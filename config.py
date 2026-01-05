import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")
    
    # It looks for a DATABASE_URL in .env, otherwise creates a local 'app.db'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    
    # Recommended: Disable overhead of tracking modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join('static', 'uploads', 'gallery')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    