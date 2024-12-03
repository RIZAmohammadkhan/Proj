from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Prompt, Folder
from app import db
from datetime import datetime
from sqlalchemy import or_
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

main = Blueprint('main', __name__)

class PromptForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    folder = HiddenField('Folder')

@main.route("/move_prompt", methods=['POST'])
@login_required
def move_prompt():
    data = request.get_json()
    prompt_id = data.get('prompt_id')
    folder_id = data.get('folder_id')
    
    prompt = Prompt.query.get_or_404(prompt_id)
    
    # Check if user owns the prompt
    if prompt.user_id != current_user.id:
        return jsonify({'success': False, 'message': 'You do not have permission to move this prompt.'})
    
    # If folder_id is empty string, set to None (uncategorized)
    prompt.folder_id = None if folder_id == '' else folder_id
    
    try:
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        search_query = request.args.get('q', '').strip()
        
        if search_query:
            # Get all prompts that match the search criteria
            matching_prompts = Prompt.query.filter(
                Prompt.user_id == current_user.id,
                or_(
                    Prompt.title.ilike(f'%{search_query}%'),
                    Prompt.content.ilike(f'%{search_query}%')
                )
            ).all()
            
            # Organize matching prompts into folders
            folder_dict = {}
            uncategorized_prompts = []
            
            for prompt in matching_prompts:
                if prompt.folder_id:
                    if prompt.folder_id not in folder_dict:
                        folder = Folder.query.get(prompt.folder_id)
                        if folder:
                            folder.prompts = []
                            folder_dict[folder.id] = folder
                    folder_dict[prompt.folder_id].prompts.append(prompt)
                else:
                    uncategorized_prompts.append(prompt)
            
            folders = list(folder_dict.values())
            return render_template('home.html', 
                                folders=folders, 
                                prompts=uncategorized_prompts,
                                search_query=search_query)
        else:
            # Get all folders and their prompts
            folders = Folder.query.filter_by(user_id=current_user.id).all()
            for folder in folders:
                folder.prompts = Prompt.query.filter_by(folder_id=folder.id).all()
            prompts = Prompt.query.filter_by(user_id=current_user.id, folder_id=None).all()
            return render_template('home.html', folders=folders, prompts=prompts)
    return render_template('landing.html')

@main.route("/create_folder", methods=['POST'])
@login_required
def create_folder():
    name = request.form.get('name')
    if name:
        # Check if folder with same name exists for this user
        existing_folder = Folder.query.filter_by(user_id=current_user.id, name=name).first()
        if existing_folder:
            flash('A folder with this name already exists.', 'danger')
            return redirect(url_for('main.home'))
            
        folder = Folder(name=name, user_id=current_user.id)
        db.session.add(folder)
        db.session.commit()
        flash('Folder created successfully!', 'success')
    return redirect(url_for('main.home'))

@main.route("/delete_folder/<int:folder_id>", methods=['POST'])
@login_required
def delete_folder(folder_id):
    folder = Folder.query.get_or_404(folder_id)
    if folder.user_id != current_user.id:
        flash('You do not have permission to delete this folder.', 'danger')
        return redirect(url_for('main.home'))
    
    # Delete all prompts in the folder
    Prompt.query.filter_by(folder_id=folder.id).delete()
    
    # Delete the folder
    db.session.delete(folder)
    db.session.commit()
    flash('Folder and all its prompts deleted successfully!', 'success')
    return redirect(url_for('main.home'))

@main.route("/create_prompt", methods=['GET', 'POST'])
@login_required
def create_prompt():
    form = PromptForm()
    folders = Folder.query.filter_by(user_id=current_user.id).all()
    
    if form.validate_on_submit():
        folder_id = form.folder.data if form.folder.data else None
        prompt = Prompt(
            title=form.title.data,
            content=form.content.data,
            folder_id=folder_id,
            user_id=current_user.id
        )
        db.session.add(prompt)
        db.session.commit()
        return redirect(url_for('main.home'))
    
    return render_template('create_prompt.html', form=form, folders=folders)

@main.route("/edit_prompt/<int:prompt_id>", methods=['GET', 'POST'])
@login_required
def edit_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    if prompt.user_id != current_user.id:
        flash('You do not have permission to edit this prompt.', 'danger')
        return redirect(url_for('main.home'))
        
    form = PromptForm(obj=prompt)
    folders = Folder.query.filter_by(user_id=current_user.id).all()
    
    if form.validate_on_submit():
        prompt.title = form.title.data
        prompt.content = form.content.data
        prompt.folder_id = form.folder.data if form.folder.data else None
        db.session.commit()
        return redirect(url_for('main.home'))
    
    return render_template('edit_prompt.html', form=form, prompt=prompt, folders=folders)

@main.route("/delete_prompt/<int:prompt_id>", methods=['POST'])
@login_required
def delete_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    if prompt.user_id != current_user.id:
        flash('You do not have permission to delete this prompt.', 'danger')
        return redirect(url_for('main.home'))
        
    db.session.delete(prompt)
    db.session.commit()
    flash('Prompt deleted successfully!', 'success')
    return redirect(url_for('main.home')) 