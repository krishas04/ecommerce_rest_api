import jwt
import datetime
from flask import current_app
from extensions import db
from models.user import User

class AuthService:

    @staticmethod
    def register(email, password):
        if User.query.filter_by(email=email).first():
            raise ValueError("User already exists.")
        
        new_user=User(email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully", "email": email}

    @staticmethod
    def login(email, password):
        user=User.query.filter_by(email=email).first()
        if not user or user.password!=password:
            raise ValueError("Invalid credentials.")

        # Generate JWT
        token = jwt.encode(
            {
                "user": email,
                "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return {"token": token}