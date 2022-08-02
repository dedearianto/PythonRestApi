from flask_restful import Resource
from flask import request
from models.product import ProductModel
from schemas.product import ProductSchema
import datetime

NAME_ALREADY_EXISTS = "A product with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the product."
PRODUCT_NOT_FOUND = "Product not found."
PRODUCT_DELETED = "Product deleted."
LOGO_ALREADY_EXISTS = "Please choose other logo!!!"

product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)


class Product(Resource):
    @classmethod
    def get(cls, name: str):
        product = ProductModel.find_by_name(name)
        if product:
            return product_schema.dump(product), 200

        return {"message": PRODUCT_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if ProductModel.find_by_name(name):
            return {"message": NAME_ALREADY_EXISTS.format(name)}, 400

        product_json = request.get_json()
        product_json["name"] = name
        product = product_schema.load(product_json)

        if ProductModel.find_by_logo_id(product.logo_id):
            return {"message": LOGO_ALREADY_EXISTS.format(product.logo_id)}, 400
        try:
            product.save_to_db()
        except Exception as e:
            return {"message": ERROR_INSERTING + " " + str(e)}, 500

        return product_schema.dump(product), 201

    @classmethod
    def delete(cls, name: str):
        product = ProductModel.find_by_name(name)
        if product:
            product.delete_from_db()
            return {"message": PRODUCT_DELETED}, 200

        return {"message": PRODUCT_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
        product_json = request.get_json()
        product = ProductModel.find_by_name(name)

        if product:
            product.description = product_json["description"]
            product.logo_id = product_json["logo_id"]
            product.updated_at = datetime.datetime.utcnow()
        else:
            product_json["name"] = name
            product = product_schema.load(product_json)

        product.save_to_db()

        return product_schema.dump(product), 200


class ProductList(Resource):
    @classmethod
    def get(cls):
        return {"products": product_list_schema.dump(ProductModel.find_all())}, 200
