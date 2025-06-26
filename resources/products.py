from flask_restful import Resource
from flask import request
from models import Product
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
# from utils.decorators import admin_required

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return [p.to_dict() for p in products], 200

    @jwt_required()
    # @admin_required
    def post(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or user.role != "admin":
            return {"error": "Admin access required"}, 403

        data = request.get_json()

        new_product = Product(
            title=data.get("title"),
            description=data.get("description"),
            price=data.get("price"),
            stock=data.get("stock"),
            image_url=data.get("image_url") or "https://via.placeholder.com/150"
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict(), 201


class ProductDetailResource(Resource):
    def get(self, id):
        product = Product.query.get_or_404(id)
        return product.to_dict(), 200

    @jwt_required()
    # @admin_required
    def patch(self, id):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or user.role != "admin":
            return {"error": "Admin access required"}, 403

        product = Product.query.get_or_404(id)
        data = request.get_json()

        for attr in ["title", "description", "price", "stock", "image_url"]:
            if attr in data:
                setattr(product, attr, data[attr])

        db.session.commit()
        return product.to_dict(), 200

    @jwt_required()
    # @admin_required
    def delete(self, id):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or user.role != "admin":
            return {"error": "Admin access required"}, 403

        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}, 204