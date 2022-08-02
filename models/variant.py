from typing import List
from sqlalchemy import func
from db import db


class VariantModel(db.Model):
    __tablename__ = "variants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    size = db.Column(db.String(5))
    color = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    product = db.relationship("ProductModel")

    def __repr__(self):
        return '<id {}> <name {}> <size {}><color {}>'.format(self.id).format(self.name).format(self.size).format(self.color)

    @classmethod
    def find_by_name(cls, name: str) -> "ProductModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["ProductModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
