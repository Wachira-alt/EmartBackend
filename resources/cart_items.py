from flask_restful import Resource
from flask import request
from models import CartItem, Product, User
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class CartItemListResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        items = CartItem.query.filter_by(user_id=user_id).all()
        return [item.to_dict() for item in items], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        # Check if item already exists — update instead
        existing_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
        if existing_item:
            existing_item.quantity += quantity
        else:
            new_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
            db.session.add(new_item)

        db.session.commit()
        return {"message": "Item added to cart"}, 201
class CartItemDetailResource(Resource):
    @jwt_required()
    def patch(self, id):
        data = request.get_json()
        quantity = data.get("quantity")

        item = CartItem.query.get_or_404(id)
        if item.user_id != get_jwt_identity():
            return {"error": "Unauthorized"}, 403

        item.quantity = quantity
        db.session.commit()
        return item.to_dict(), 200

    @jwt_required()
    def delete(self, id):
        item = CartItem.query.get_or_404(id)
        if item.user_id != get_jwt_identity():
            return {"error": "Unauthorized"}, 403

        db.session.delete(item)
        db.session.commit()
        return {"message": "Item removed from cart"}, 204
