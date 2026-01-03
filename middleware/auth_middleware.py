from functools import wraps
from flask import request,current_app, g , jsonify
import jwt

def token_required(f):
  @wraps(f)
  def decorated(*args,**kwargs):
    token=request.headers.get("Authorization")
    if not token:
      return jsonify({"error":"Token is missing."}),401
    
    try:
      token=token.replace("Bearer","")
      data=jwt.decode(token,current_app.config["SECRET_KEY"],algorithms="HS256")
      g.user_email=data["user"]
    except jwt.ExpiredSignatureError:
      return jsonify({"error":"Token is expired"}),401
    except jwt.InvalidTokenError:
      return jsonify({"error":"Invalid token"}),401
    
    return f(*args,**kwargs)
  return decorated