# Todo Application
A simple Django-based Todo application for managing tasks.

# Features
Add, view, and delete tasks.
Tasks are displayed dynamically using Django templates.
SQLite is used as the database backend.
# Setup Instructions
# Prerequisites
Python
pip (Python package manager)
git (version control)
Steps to Set Up
# Clone the Repository

git clone http:github.com/AvinashK47/Todo
cd Todo
Set Up Virtual Environment

bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
# Install Dependencies
in terminal/bash

pip install -r requirements.txt
Database Setup

bash
python manage.py makemigrations
python manage.py migrate
# Run the Development Server

bash

python manage.py runserver
Open your browser and visit: http://localhost:8000

Project Structure
php
Copy code
Todo/
├── tasks/            # Main app for managing tasks
│   ├── migrations/   # Database migrations
│   ├── templates/    # HTML templates
│   ├── static/       # Static files (CSS, JS)
│   ├── views.py      # Application logic
│   ├── models.py     # Task model
├── Todo/             # Main project settings
│   ├── settings.py   # Project settings
│   ├── urls.py       # URL routing
├── db.sqlite3        # SQLite database
├── manage.py         # Django's management script
├── requirements.txt  # Dependencies

# Necessary
If made modifications to the tasks model or any other models gets added or altered : 
python manage.py makemigrations
python manage.py migrate
