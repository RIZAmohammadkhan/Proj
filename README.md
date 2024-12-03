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

## Quick Start

1. Clone the repository using VS Code:
   - Open VS Code
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type "Git: Clone"
   - Paste the repository URL
   - Select a local folder

2. Set up Python environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment:
   ```bash
   # Copy example environment file
   cp .env.example .env
   ```

5. Set up Gmail for email verification:
   - Go to your [Google Account Security Settings](https://myaccount.google.com/security)
   - Enable 2-Step Verification if not enabled
   - Create an App Password:
     1. Go to Security → 2-Step Verification → App passwords
     2. Select 'Mail' and your device
     3. Copy the generated 16-character password
   - Update `.env` file with:
     ```
     EMAIL_USER=your-gmail@gmail.com
     EMAIL_PASS=your-16-char-app-password
     ```

6. Initialize database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

7. Run the application:
   ```bash
   python run.py
   ```

## VS Code Development Setup

1. Recommended extensions:
   - Python (Microsoft)
   - Python Indent
   - GitLens
   - SQLite Viewer
   - Prettier

2. Workspace settings (`.vscode/settings.json`):
   ```json
   {
     "python.linting.enabled": true,
     "python.linting.flake8Enabled": true,
     "editor.formatOnSave": true,
     "python.formatting.provider": "black"
   }
   ```

## Email Verification System

The application implements a secure email verification system:

1. Registration Process:
   - User registers with email and password
   - Account is created in an unverified state
   - Verification email is sent with a secure token
   - Token expires after 1 hour for security

2. Verification:
   - User clicks link in email
   - Token is validated
   - Account is marked as verified
   - User can now log in

3. Security Features:
   - Time-limited tokens (1 hour expiry)
   - Secure token generation using URLSafeTimedSerializer
   - Protection against token tampering
   - One-time use tokens

## Database Structure

```sql
User
- id (Primary Key)
- username (Unique)
- email (Unique)
- password (Hashed)
- email_verified (Boolean)

Folder
- id (Primary Key)
- name
- user_id (Foreign Key)
- created_at

Prompt
- id (Primary Key)
- title
- content
- folder_id (Foreign Key, Optional)
- user_id (Foreign Key)
- created_at
- updated_at
```

## API Routes

### Authentication
- `/register` - User registration
- `/login` - User login
- `/logout` - User logout
- `/verify_email/<token>` - Email verification

### Prompts
- `/` - Home/Dashboard
- `/create_prompt` - Create new prompt
- `/edit_prompt/<id>` - Edit existing prompt
- `/delete_prompt/<id>` - Delete prompt

### Folders
- `/create_folder` - Create new folder
- `/delete_folder/<id>` - Delete folder and its prompts

## Error Handling

The application includes comprehensive error handling:
- Invalid email verification tokens
- Expired tokens
- Database constraints
- Form validation
- Authentication errors

## Security Considerations

1. Password Security:
   - Passwords are hashed using Bcrypt
   - Minimum password requirements enforced
   - Protection against brute force attacks

2. Email Security:
   - Secure token generation
   - Limited token validity
   - Protection against email spoofing

3. Data Protection:
   - CSRF protection on all forms
   - Secure session handling
   - Input validation and sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please:
1. Check existing issues
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected behavior
   - Screenshots if applicable