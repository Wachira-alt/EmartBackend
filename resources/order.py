from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import CartItem, Order, OrderItem, Product, User
from utils.decorators import admin_required
from extensions import db

class CheckoutResource(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        cart_items = CartItem.query.filter_by(user_id=user_id).all()
        if not cart_items:
            return {"error": "Cart is empty"}, 400

        order = Order(user_id=user_id)
        db.session.add(order)
        db.session.flush()  # So order.id is available

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_purchase=item.product.price  # snapshot price
            )
            db.session.add(order_item)
            db.session.delete(item)  # Clear from cart

        db.session.commit()
        return order.to_dict(), 201
    
class UserOrdersResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        orders = [order.to_dict() for order in user.orders]
        return orders, 200
class AdminOrderListResource(Resource):
    @jwt_required()
    @admin_required  # Protect this route
    def get(self):
        orders = Order.query.all()
        return [order.to_dict() for order in orders], 200
class AdminOrderCancelResource(Resource):
    @jwt_required()
    @admin_required
    def patch(self, order_id):
        order = Order.query.get_or_404(order_id)
        if order.status == "cancelled":
            return {"error": "Already cancelled"}, 400

        order.status = "cancelled"
        db.session.commit()
        return order.to_dict(), 200
    
class AdminOrderStatusResource(Resource):
    @jwt_required()
    @admin_required
    def patch(self, order_id):
        order = Order.query.get_or_404(order_id)
        data = request.get_json()
        new_status = data.get("status")

        valid_statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]
        if new_status not in valid_statuses:
            return {"error": "Invalid status"}, 400

        order.status = new_status
        db.session.commit()
        return order.to_dict(), 200