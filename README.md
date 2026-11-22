# Employee Management System

A Python-based Employee Management System that helps manage employee records through a console application and a web interface built using Flask.

## Project Overview

The Employee Management System is designed to simplify employee record management. It allows users to add, view, search, update, and delete employee details, along with calculating salary after bonuses and deductions.

The project started as a Python console application and was extended into a web application using Flask.

## Features

- Add new employee records
- View all employee details
- Search employees using Employee ID
- Update employee department
- Delete employee records
- Calculate salary with bonus and deductions
- Store employee data using JSON
- Display employee records through a Flask web application
- Dynamic employee table using HTML and Jinja templates
- Basic input validation

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| HTML | Web page structure |
| CSS | Styling |
| JSON | Employee data storage |
| Git | Version control |
| GitHub | Project hosting |

## Project Structure

```text
employee_management/
│
├── app.py
├── employee_system.py
├── employees.json
├── .gitignore
├── .gitattributes
│
├── static/
│   └── style.css
│
└── templates/
    └── employees.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd employee_management
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Run the Flask application

```bash
python -m flask --app app run --debug
```

### 7. Open the application

Visit the following URL in your browser:

```text
http://127.0.0.1:5000/
```

## Learning Outcomes

Through this project, I practiced:

- Python variables, data types, conditions, loops and functions
- Lists and dictionaries
- File handling and JSON operations
- CRUD operations
- Flask routes and web application basics
- HTML and CSS integration
- Git and GitHub version control

## Future Improvements

- Implement a complete web-based CRUD interface
- Add employee search, update and delete functionality to the web application
- Integrate SQLite database
- Improve UI design and responsiveness
- Add form validation and error handling
- Implement automated testing

## Author

**Sharanya**

Engineering Student

Developed as a hands-on learning project to practice Python, Flask, HTML, CSS, and JSON.

---

**Note:** This project is currently under development. More features and improvements will be added as development progresses.
