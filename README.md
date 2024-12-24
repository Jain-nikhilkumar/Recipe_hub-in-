# Recipe Manager Web Application

## Overview

The Recipe Manager Web Application is a user-friendly platform for managing, organizing, and searching for recipes. Built with modern web technologies, the application features a responsive and attractive design.

## Features

- **User Authentication**:

  - Sign up and log in to your account.
  - Secure password storage and validation.

- **Recipe Management**:

  - Add, update, and delete recipes.
  - View all recipes with search functionality.

- **Responsive Design**:

  - Fully optimized for desktop and mobile devices.
  - Black and white modern theme for an elegant UI.

- **Search Functionality**:
  - Quickly find recipes by name.

---

## Tech Stack

- **Frontend**:

  - HTML5, CSS3, Bootstrap 5

- **Backend**:

  - Django (Python)

- **Database**:

  - SQLite (default for Django)

- **Version Control**:
  - Git and GitHub

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- Git

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository/recipe-manager.git
   cd recipe-manager
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate   # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:8000
   ```

---

## Usage

1. **Sign Up**:

   - Create a new account using your first name, last name, email, and password.

2. **Log In**:

   - Log in to access and manage your recipes.

3. **Manage Recipes**:

   - Add new recipes with images, descriptions, and titles.
   - Edit or delete existing recipes as needed.

4. **Search Recipes**:
   - Use the search bar to find specific recipes by name.

---

## File Structure

```
recipe-manager/
├── first/            # Backend logic and API implementation
├── media/            # Media contents in project
├── vege/             # Frontend templates and static files and Backend logic
├── manage.py         # Django project manager
├── db.sqlite3        # SQLite database file
├── .gitignore        # Ignored files and folders
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

---

## Contributing

I welcome contributions! Please fork the repository and create a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
