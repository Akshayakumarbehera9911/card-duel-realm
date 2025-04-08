import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Create Flask application
app = Flask(__name__)

# Configure database
database_url = os.environ.get("DATABASE_URL", "mysql+pymysql://root:0000@localhost:3306/card_game")

# Handle potential SSL requirements for some providers
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_secret_key_for_development")

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Create tables and seed database
with app.app_context():
    # Import models after db is defined to avoid circular imports
    from models import Card
    
    print("Creating database tables...")
    db.create_all()
    
    # Import and run seed function
    from seed_db import seed_database
    seed_database()

# Import and register routes
from routes import register_routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)