from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt, mail
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import os

auth = Blueprint('auth', __name__)
serializer = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))

def send_verification_email(user_email):
    token = serializer.dumps(user_email, salt='email-verification-salt')
    msg = Message('Verify Your Email',
                  sender='noreply@promptmanager.com',
                  recipients=[user_email])
    
    verification_url = url_for('auth.verify_email', token=token, _external=True)
    
    msg.body = f'''To verify your email, visit the following link:
{verification_url}

If you did not make this request then simply ignore this email.
'''
    mail.send(msg)

@auth.route("/verify_email/<token>")
def verify_email(token):
    try:
        email = serializer.loads(token, salt='email-verification-salt', max_age=3600)  # Token expires in 1 hour
        user = User.query.filter_by(email=email).first()
        if user:
            user.email_verified = True
            db.session.commit()
            flash('Your email has been verified! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
    except:
        flash('The verification link is invalid or has expired.', 'danger')
    return redirect(url_for('auth.login'))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, email_verified=False)
        db.session.add(user)
        db.session.commit()
        send_verification_email(user.email)
        flash('Account created! Please check your email to verify your account.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.email_verified:
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
            else:
                flash('Please verify your email before logging in. Check your inbox for the verification link.', 'warning')
                return redirect(url_for('auth.login'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home')) 