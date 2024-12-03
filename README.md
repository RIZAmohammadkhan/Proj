# Prompt Manager

A modern, minimalist Flask web application for creating, organizing, and managing prompts with a beautiful user interface and secure authentication system.

## Features

### Authentication & Security
- Secure user registration with email verification
- Password encryption using Bcrypt
- Protected routes with Flask-Login
- CSRF protection
- Email verification system using secure tokens

### Prompt Management
- Create, edit, and delete prompts
- Rich text editing with Markdown support
- Organize prompts into folders
- Search functionality for prompt titles and content
- Move prompts between folders
- Uncategorized prompts section

### User Interface
- Modern, minimalistic design
- Dark mode support
- Responsive layout
- Real-time Markdown preview
- Side-by-side editing mode
- Fullscreen editing support

### Technical Features
- Flask-based backend
- SQLAlchemy ORM
- Flask-Mail for email verification
- Database migrations with Flask-Migrate
- Environment variable configuration
- CSRF protection with Flask-WTF

## Technology Stack

- **Backend**: Flask 3.0.0
- **Database**: SQLAlchemy with Flask-SQLAlchemy 3.1.1
- **Authentication**: Flask-Login 0.6.3
- **Forms**: Flask-WTF 1.2.1
- **Password Hashing**: Flask-Bcrypt 1.0.1
- **Email**: Flask-Mail
- **Database Migrations**: Flask-Migrate 4.0.5
- **Environment Variables**: python-dotenv 1.0.0

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd prompt-manager
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following:
   ```
   SECRET_KEY=your_secure_secret_key_here
   EMAIL_USER=your-gmail@gmail.com
   EMAIL_PASS=your-app-specific-password
   ```

5. Set up Gmail for email verification:
   - Enable 2-Step Verification in your Google Account
   - Generate an App Password:
     1. Go to Google Account Settings
     2. Navigate to Security
     3. Under "2-Step Verification", select "App passwords"
     4. Generate a password for Mail
     5. Use this password as EMAIL_PASS in .env

6. Initialize the database:
   ```bash
   flask db upgrade
   ```

7. Run the application:
   ```bash
   python run.py
   ```

## Usage

1. Register a new account
2. Verify your email through the verification link
3. Login with your credentials
4. Create folders to organize your prompts
5. Create new prompts with the rich text editor
6. Use the search functionality to find specific prompts
7. Organize prompts by moving them between folders

## Project Structure

```
prompt-manager/
├── app/
│   ├── __init__.py      # Application factory and extensions
│   ├── models.py        # Database models
│   ├── routes.py        # Main routes
│   ├── auth.py         # Authentication routes
│   ├── static/         # Static files (CSS, JS)
│   └── templates/      # HTML templates
├── instance/           # Instance-specific files
├── migrations/         # Database migrations
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── run.py             # Application entry point
```

## Security Features

- Password hashing with Bcrypt
- Email verification with time-limited tokens
- CSRF protection on all forms
- Secure session handling
- Protected routes requiring authentication
- Secure password reset functionality

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Development

To set up the development environment:

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Run tests:
   ```bash
   python -m pytest
   ```

3. Check code style:
   ```bash
   flake8
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask and its extensions
- SimpleMDE for Markdown editing
- Bootstrap for base styling
- Font Awesome for icons 