from flask_restful import Api
from flask import Blueprint
from .auth import RegisterResource, LoginResource, ProfileResource
from .products import ProductListResource, ProductDetailResource
from .cart_items import CartItemListResource, CartItemDetailResource
from .order import CheckoutResource, AdminOrderListResource, AdminOrderCancelResource, AdminOrderStatusResource, UserOrdersResource
from resources.users import AdminUserListResource, PromoteUserResource, DeleteUserResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Auth routes
api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")
api.add_resource(ProfileResource, "/profile")

#product endpoints

api.add_resource(ProductListResource, "/products")
api.add_resource(ProductDetailResource, "/products/<int:id>")

# #cart items
api.add_resource(CartItemListResource, "/cart-items")
api.add_resource(CartItemDetailResource, "/cart-items/<int:id>")

# checkout resource
api.add_resource(CheckoutResource, "/orders/checkout")
api.add_resource(AdminOrderListResource, '/orders')
api.add_resource(AdminOrderCancelResource, "/orders/<int:order_id>/cancel")
api.add_resource(AdminOrderStatusResource, "/orders/<int:order_id>/status")
api.add_resource(UserOrdersResource, "/orders/me")




# getting users by admin

api.add_resource(AdminUserListResource, "/users")
api.add_resource(PromoteUserResource, "/users/<int:user_id>/promote")
api.add_resource(DeleteUserResource, "/users/<int:user_id>")