import models
import jwt
import os

class User_Auth ():
    def verify_user (id):
        decrypted_id = jwt.decode(id, os.environ.get("JWT_SECRET"), algorithms=["HS256"])["user_id"]
        user = models.User.query.filter(models.User.id == decrypted_id).first()
    
        if user:
            return user
        else:
            return None