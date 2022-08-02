from flask_restful import Resource
from flask import request
from models.variant import VariantModel
from schemas.variant import VariantSchema
import datetime

NAME_ALREADY_EXISTS = "A variant with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the variant."
VARIANT_NOT_FOUND = "Product not found."
VARIANT_DELETED = "Product deleted."


variant_schema = VariantSchema()
variant_list_schema = VariantSchema(many=True)


class Variant(Resource):
    @classmethod
    def get(cls, name: str):
        variant = VariantModel.find_by_name(name)
        if variant:
            return variant_schema.dump(variant), 200

        return {"message": VARIANT_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if VariantModel.find_by_name(name):
            return {"message": NAME_ALREADY_EXISTS.format(name)}, 400

        variant_json = request.get_json()
        variant_json["name"] = name
        variant = variant_schema.load(variant_json)

        try:
            variant.save_to_db()
        except Exception as e:
            return {"message": ERROR_INSERTING + " " + str(e)}, 500

        return variant_schema.dump(variant), 201

    @classmethod
    def delete(cls, name: str):
        variant = VariantModel.find_by_name(name)
        if variant:
            variant.delete_from_db()
            return {"message": VARIANT_DELETED}, 200

        return {"message": VARIANT_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
        variant_json = request.get_json()
        variant = VariantModel.find_by_name(name)

        if variant:
            variant.product_id = variant_json["product_id"]
            variant.size = variant_json["size"]
            variant.color = variant_json["color"]
            variant.updated_at = datetime.datetime.utcnow()
        else:
            variant_json["name"] = name
            variant = variant_schema.load(variant_json)

        variant.save_to_db()

        return variant_schema.dump(variant), 200


class VariantList(Resource):
    @classmethod
    def get(cls):
        return {"products": variant_list_schema.dump(VariantModel.find_all())}, 200
