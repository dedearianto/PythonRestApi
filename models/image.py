from typing import List

from db import db


class ImageModel(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(5000), nullable=False, unique=True)

    products = db.relationship("ProductModel", backref="ImageModel")


    @classmethod
    def find_by_url(cls, url: str) -> "ImageModel":
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_all(cls) -> List["ImageModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
