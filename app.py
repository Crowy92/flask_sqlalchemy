from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Init db
db = SQLAlchemy(app)
# Init marshmallow
ma = Marshmallow(app)

# Product -------------------------------------------------------------------------------------------------------------------------------------
# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "qty")


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route("/product", methods=["POST"])
def add_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get all products
@app.route("/product", methods=["GET"])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)


# Get single product
@app.route("/product/<id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)


# Update a Product
@app.route("/product/<id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)


# Delete single product
@app.route("/product/<id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return {"msg": "Item Deleted"}


# User ----------------------------------------------------------------------------------------------------------------------
# User Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(40))
    age = db.Column(db.Integer)
    location = db.Column(db.String(100))
    choice1 = db.Column(db.String(40))
    choice2 = db.Column(db.String(40))
    choice3 = db.Column(db.String(40))
    choice4 = db.Column(db.String(40))

    def __init__(
        self, name, email, password, age, location, choice1, choice2, choice3, choice4
    ):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.location = location
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4


# user Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "email",
            "password",
            "age",
            "location",
            "choice1",
            "choice2",
            "choice3",
            "choice4",
        )


# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a user
@app.route("/user", methods=["POST"])
def add_user():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    age = request.json["age"]
    location = request.json["location"]
    choice1 = request.json["choice1"]
    choice2 = request.json["choice2"]
    choice3 = request.json["choice3"]
    choice4 = request.json["choice4"]

    new_user = User(
        name, email, password, age, location, choice1, choice2, choice3, choice4
    )

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# Get all users
@app.route("/user", methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Get single user
@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# Update a user
@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)

    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    age = request.json["age"]
    location = request.json["location"]
    choice1 = request.json["choice1"]
    choice2 = request.json["choice2"]
    choice3 = request.json["choice3"]
    choice4 = request.json["choice4"]

    user.name = name
    user.email = email
    user.password = password
    user.age = age
    user.location = location
    user.choice1 = choice1
    user.choice2 = choice2
    user.choice3 = choice3
    user.choice4 = choice4

    db.session.commit()

    return user_schema.jsonify(user)


# Delete single user
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return {"msg": "Item Deleted"}


# Runserver
if __name__ == "__main__":
    app.run(debug=True)
