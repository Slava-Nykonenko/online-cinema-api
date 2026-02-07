from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    genre: str
    price: float

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
