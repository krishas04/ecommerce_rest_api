# REST E-Commerce API

This is a REST-based E-Commerce API built using Flask and SQLAlchemy.
The API supports product management, authentication, and order processing.

***

## Features
- RESTful API architecture
- JWT-based authentication
- Product, category, and order management
- SQLAlchemy ORM
- Marshmallow serialization
- API testing using Insomnia

***

## Technologies Used
- Python
- Flask
- SQLAlchemy
- Marshmallow
- JWT
- SQLite
- Insomnia (API Client)

***

## How to Run the Project

### 1. Clone the Repository
```bash
git clone <repository-url>
cd rest_ecommerce

### 2. Create Virtual Environment for windows
python -m venv venv

Activate it:
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Environment Variables
Create a .env file and add:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key

### 5. Initialize Database
python app.py
or
flask run

### API Testing
Use Insomnia to:

  -Send HTTP requests

  -Test JWT authentication

  -Debug API responses

### Project Structure
REST_ECOMMERCE/
│
├── api/                    # API route definitions (Blueprints / endpoints)
│
├── instance/               # Instance-specific data (SQLite DB)
│
├── middleware/             # Custom middleware (auth checks)
│
├── migrations/             # Database migration files (Flask-Migrate)
│
├── models/                 # Database models (SQLAlchemy ORM)
│
├── schemas/                # Serialization & validation schemas (Marshmallow)
│
├── services/               # Business logic layer
│
├── static/                 # Static files where images are uploaded
│
├── utils/                  # Helper and utility functions related to datetime
│
├── views/                  # Request/response handlers (controllers)
│
├── venv/                   # Python virtual environment
│
├── .env                    # Environment variables
│
├── .gitignore              # Git ignored files
│
├── app.py                  # Application entry point
│
├── config.py               # Application configuration
│
├── extensions.py           # Initialized extensions (db, migrate, jwt, etc.)
│
├── requirements.txt        # Project dependencies
│
├── README.md               
│
└── topics_to_cover.md      

