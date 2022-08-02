from typing import List
from sqlalchemy import func
from db import db


class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)

    logo_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False, unique=True)
    image = db.relationship("ImageModel")

    def __repr__(self):
        return '<id {}> <name {}> <description {}>'.format(self.id).format(self.name).format(self.description)

    @classmethod
    def find_by_name(cls, name: str) -> "ProductModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_logo_id(cls, logo_id: int) -> "ProductModel":
        return cls.query.filter_by(logo_id=logo_id).first()

    @classmethod
    def find_all(cls) -> List["ProductModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
