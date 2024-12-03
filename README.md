# Prompt Manager

A Flask-based web application for organizing and managing prompts in a structured way. Users can create, edit, and organize prompts into folders while maintaining a secure and personalized workspace.

## Features

- **User Authentication**
  - Secure user registration and login
  - Password encryption using Bcrypt
  - Protected routes with Flask-Login

- **Prompt Management**
  - Create, edit, and delete prompts
  - Organize prompts into folders
  - Search functionality for prompt titles and content
  - Move prompts between folders
  - Uncategorized prompts section

- **Folder Organization**
  - Create and delete folders
  - Drag-and-drop prompt organization
  - Hierarchical structure for better organization

## Technology Stack

- **Backend**: Flask 3.0.0
- **Database**: SQLAlchemy with Flask-SQLAlchemy 3.1.1
- **Authentication**: Flask-Login 0.6.3
- **Forms**: Flask-WTF 1.2.1
- **Password Hashing**: Flask-Bcrypt 1.0.1
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

4. Create a `.env` file in the root directory and add your configuration:
   ```
   SECRET_KEY=your_secret_key_here
   ```

5. Initialize the database:
   ```bash
   flask db upgrade
   ```

6. Run the application:
   ```bash
   python run.py
   ```

## Usage

1. Register a new account or login with existing credentials
2. Create folders to organize your prompts
3. Add new prompts with titles and content
4. Use the search functionality to find specific prompts
5. Organize prompts by moving them between folders
6. Edit or delete prompts and folders as needed

## Project Structure

```
prompt-manager/
├── app/
│   ├── __init__.py      # Application factory and extensions
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes
│   ├── auth.py         # Authentication routes
│   ├── static/         # Static files (CSS, JS)
│   └── templates/      # HTML templates
├── instance/           # Instance-specific files
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── run.py             # Application entry point
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 