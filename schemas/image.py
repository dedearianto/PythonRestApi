from ma import ma
from models.image import ImageModel



class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ImageModel
        dump_only = ("id",)
        load_instance = True
