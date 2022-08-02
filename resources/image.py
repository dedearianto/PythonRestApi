from flask_restful import Resource
from flask import request
from models.image import ImageModel
from schemas.image import ImageSchema

URL_ALREADY_EXISTS = "An image  with url '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the image."
IMAGE_NOT_FOUND = "Image not found."
IMAGE_DELETED = "Image deleted."

image_schema = ImageSchema()
image_list_schema = ImageSchema(many=True)


class Image(Resource):
    @classmethod
    def get(cls, url: str):
        image = ImageModel.find_by_url(url)
        if image:
            return image_schema.dump(image), 200

        return {"message": IMAGE_NOT_FOUND}, 404

    @classmethod
    def post(cls):
        image_json = request.get_json()
        image = image_schema.load(image_json)

        if ImageModel.find_by_url(image.url):
            return {"message": URL_ALREADY_EXISTS.format(image.url)}, 400

        try:
            image.save_to_db()
        except Exception as e:
            return {"message": ERROR_INSERTING +" " +str(e)}, 500

        return image_schema.dump(image), 201

    @classmethod
    def delete(cls, url: str):
        image = ImageModel.find_by_url(url)
        if image:
            image.delete_from_db()
            return {"message": IMAGE_DELETED}, 200

        return {"message": IMAGE_NOT_FOUND}, 404

class ImageList(Resource):
    @classmethod
    def get(cls):
        return {"items": image_list_schema.dump(ImageModel.find_all())}, 200
