from sqlalchemy.orm import Session
from . import models, schemas

def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Image).offset(skip).limit(limit).all()

def get_image_by_name(db: Session, name: str):
    return db.query(models.Image).filter(models.Image.name == name).first()

def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
