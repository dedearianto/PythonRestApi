from ma import ma
from models.product import ProductModel
from schemas.image import ImageSchema


class ProductSchema(ma.SQLAlchemyAutoSchema):
    image = ma.Nested(ImageSchema)
    class Meta:
        model = ProductModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
