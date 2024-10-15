from pydantic import BaseModel

class ImageBase(BaseModel):
    name: str
    confidence: float
    xmin_x: float
    ymin_y: float
    xmax_x: float
    ymax_y: float

class ImageCreate(ImageBase):
    pass

class ImageResponse(ImageBase):
    class Config:
        orm_mode = True
