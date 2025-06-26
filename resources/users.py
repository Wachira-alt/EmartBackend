from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models import User
from utils.decorators import admin_required
from extensions import db

class AdminUserListResource(Resource):
    @jwt_required()
    @admin_required
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200
# PATCH /users/<id>/promote
class PromoteUserResource(Resource):
    @jwt_required()
    @admin_required
    def patch(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        user.role = "admin"
        db.session.commit()
        return user.to_dict(), 200

# DELETE /users/<id>
class DeleteUserResource(Resource):
    @jwt_required()
    @admin_required
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {}, 204
