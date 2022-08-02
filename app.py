from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.product import Product, ProductList
from resources.image import Image, ImageList
from resources.variant import Variant, VariantList

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/dbpython"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400



api.add_resource(Product, "/product/<string:name>")
api.add_resource(ProductList, "/products")
api.add_resource(Image, "/image")
api.add_resource(ImageList, "/images")
api.add_resource(Variant, "/variant/<string:name>")
api.add_resource(VariantList, "/variants")



if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
