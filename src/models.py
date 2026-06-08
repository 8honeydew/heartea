from pydantic import BaseModel


class Review(BaseModel):
    author: str
    rating: float
    text: str


class Place(BaseModel):
    name: str
    city: str
    category: str
    reviews: list[Review]