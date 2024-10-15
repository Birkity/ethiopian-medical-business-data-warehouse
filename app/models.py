from sqlalchemy import Column, String, Float
from .database import Base

class Image(Base):
    __tablename__ = "images"
    name = Column(String, primary_key=True)
    confidence = Column(Float)
    xmin_x = Column(Float)
    ymin_y = Column(Float)
    xmax_x = Column(Float)
    ymax_y = Column(Float)
