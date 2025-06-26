from extensions import db, bcrypt
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), default='user')  # 'user' or 'admin'

    cart_items = db.relationship('CartItem', back_populates='user', cascade="all, delete")
    orders = db.relationship('Order', back_populates='user', cascade="all, delete")

    # serialize_rules = ('-cart_items.user', '-orders.user',)
    serialize_rules = ('-cart_items', '-orders',)


    @property
    def password_hash(self):
        raise AttributeError("Password is write-only.")

    @password_hash.setter
    def password_hash(self, plain_password):
        self._password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, plain_password):
        return bcrypt.check_password_hash(self._password_hash, plain_password)

    @validates("email")
    def validate_email(self, key, value):
        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format")
        return value
