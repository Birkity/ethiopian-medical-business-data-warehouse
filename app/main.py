from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/images/", response_model=schemas.ImageResponse)
def create_image(image: schemas.ImageCreate, db: Session = Depends(get_db)):
    return crud.create_image(db=db, image=image)

@app.get("/images/", response_model=list[schemas.ImageResponse])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_images(db, skip=skip, limit=limit)

@app.get("/images/{name}", response_model=schemas.ImageResponse)
def read_image(name: str, db: Session = Depends(get_db)):
    db_image = crud.get_image_by_name(db, name=name)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image
