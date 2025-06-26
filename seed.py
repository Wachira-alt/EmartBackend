from app import create_app
from extensions import db
from models import User, Product
from werkzeug.security import generate_password_hash  # Optional fallback if needed

app = create_app()

def seed():
    with app.app_context():
        print("🧨 Dropping existing tables...")
        db.drop_all()

        print("✅ Creating tables...")
        db.create_all()

        print("👤 Seeding users...")
        admin = User(
            username="admin",
            email="admin@example.com",
            password_hash="admin123",  # Uses setter
            role="admin"
        )
        user = User(
            username="john_doe",
            email="john@example.com",
            password_hash="johnpass",
            role="user"
        )

        print("📦 Seeding products...")
        products = [
            Product(
                title="Custom Notebook",
                description="Personalized eco-friendly notebook.",
                price=450.00,
                image_url="https://via.placeholder.com/150",
                stock=30
            ),
            Product(
                title="Pen Set (5pcs)",
                description="Smooth gel pens in assorted colors.",
                price=250.00,
                image_url="https://via.placeholder.com/150",
                stock=50
            ),
            Product(
                title="A4 Paper - 500 sheets",
                description="High-quality multipurpose paper.",
                price=600.00,
                image_url="https://via.placeholder.com/150",
                stock=20
            )
        ]

        db.session.add_all([admin, user] + products)
        db.session.commit()
        print("🌱 Seed data inserted successfully!")

if __name__ == "__main__":
    seed()
