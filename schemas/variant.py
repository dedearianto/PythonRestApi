from ma import ma
from models.variant import VariantModel
from schemas.product import ProductSchema

class VariantSchema(ma.SQLAlchemyAutoSchema):
    product = ma.Nested(ProductSchema)
    class Meta:
        model = VariantModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
