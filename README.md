
# EMART Backend - Personalized Stationery E-Commerce API

## Description

The EMART backend is a RESTful API built with Flask. It powers the EMART personalized stationery e-commerce platform, handling authentication, product management, cart functionality, order processing, and admin operations. The backend uses PostgreSQL with SQLAlchemy for database management, Flask-JWT-Extended for authentication, and Flask-CORS for cross-origin resource sharing.

### Tech Stack

- Framework: Flask
- Database: PostgreSQL
- Authentication: JWT-based

---

## Features

### User Authentication & Authorization

- User registration and login
- JWT-based token authentication
- Role-based access control (Admin, Customer)
- Password reset functionality (optional)

### Product Management

- Admin-only CRUD operations for products
- Category support
- Search and filtering
- Image upload and storage
- Inventory tracking

### Shopping Cart & Orders

- Add to cart, update quantities, remove items
- Order placement and order history
- Order status management

### Admin Panel

- User management
- Product and order management
- Basic sales analytics support

---

## File Structure

```plaintext
EMARTBACKEND/
├── app.py                 # Application factory
├── config.py              # App configuration
├── .env.example           # Environment variable example
├── Pipfile                # Dependencies
├── Pipfile.lock
├── README.md              # Project documentation
├── seed.py                # Seed script for initial data
├── schemas.py             # Marshmallow schemas (optional)
├── extensions.py          # Initialized extensions
├── utils/
│   └── decorators.py      # Custom decorators
├── models/
│   ├── __init__.py
│   ├── cart_item.py
│   ├── order_item.py
│   ├── order.py
│   ├── product.py
│   └── user.py
└── resources/
    ├── __init__.py
    ├── auth.py
    ├── cart_items.py
    ├── order.py
    ├── products.py
    └── users.py
````

---

## Setup Instructions

### Prerequisites

* Python 3.9+
* PostgreSQL installed and running
* Git

---

### Installation

1. Clone the Repository

   ```bash
   git clone <your-backend-repo-url>
   cd emart-backend
   ```

2. Install Dependencies

   ```bash
   pip install flask flask-jwt-extended flask-sqlalchemy flask-cors psycopg2-binary werkzeug python-dotenv
   ```

3. Configure the Database

   * Create a PostgreSQL database named `emart_db`.
   * Either:

     * Set credentials in `config.py`, or
     * Use a `.env` file with `DATABASE_URL=postgresql://username:password@localhost:5432/emart_db`.

4. Initialize the Database

   You can run the Flask app once to create all tables automatically:

   ```bash
   python app.py
   ```

5. Run the Backend Server

   ```bash
   python app.py
   ```

---

## Usage

### Authentication

* **Register**
  `POST /api/auth/register`
  Payload: `{ "email": "user@example.com", "password": "password" }`

* **Login**
  `POST /api/auth/login`
  Returns JWT token.

### Products

* `GET /api/products` - list all products
* `POST /api/products` - add product (admin only)
* `PUT /api/products/<id>` - update product (admin only)
* `DELETE /api/products/<id>` - delete product (admin only)

### Orders

* `POST /api/orders` - create new order
* `GET /api/orders` - view user’s orders

### Cart

* `GET /api/cart` - view cart
* `POST /api/cart` - add to cart
* `PUT /api/cart/<id>` - update cart item
* `DELETE /api/cart/<id>` - remove cart item

---

## Example: Frontend Integration

* **Backend Repo**: [GitHub - Backend]()

* **Backend Deployed To**: [e.g., Render, Railway]()

* **Frontend Repo**: [GitHub - Frontend]()

* **Frontend Deployed To**: [Vercel, Netlify]()

---

## Integration Steps

### 1. Update CORS

In `app.py`:

```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "https://emart-frontend.netlify.app"}})
```

### 2. Frontend API Configuration

In the frontend's `apiEndPoints.js`:

```js
export const API_ENDPOINTS = {
  LOGIN: "<backend-url>/api/auth/login",
  REGISTER: "<backend-url>/api/auth/register",
  PRODUCTS: "<backend-url>/api/products",
  ORDERS: "<backend-url>/api/orders",
  PROFILE: "<backend-url>/api/users/me",
  CART: "<backend-url>/api/cart"
};
```

### 3. Deployment

* Push the backend to GitHub and deploy using your preferred service (e.g., Render, Railway, Fly.io).
* Make sure environment variables are configured on the platform.
* Push the frontend to GitHub and deploy via Vercel or Netlify.
* Test API calls from frontend to backend.

---

## Contributing

1. Fork the repository

2. Create a feature branch

   ```bash
   git checkout -b feature/feature-name
   ```

3. Commit your changes

   ```bash
   git commit -m "Add: new feature"
   ```

4. Push the branch

   ```bash
   git push origin feature/feature-name
   ```

5. Open a Pull Request for review


