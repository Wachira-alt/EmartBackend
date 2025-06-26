from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User
from extensions import db, bcrypt

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.query.filter_by(email=email).first():
            return {"error": "Email already registered"}, 400

        user = User(username=username, email=email)
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=user.id)
        return {"message": "User registered", "access_token": token}, 201

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            token = create_access_token(identity=user.id)
            return {"access_token": token}, 200

        return {"error": "Invalid credentials"}, 401

class ProfileResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        return user.to_dict(), 200