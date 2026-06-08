from fastapi import FastAPI, Query
from src.db import places

app = FastAPI(title="Heartea API")


@app.get("/")
def root():
    return {"message": "Heartea API is running"}


@app.get("/places")
def get_places():
    return places

@app.get("/search")
def search_places(query: str = Query(...)):
    results = []

    for place in places:
        for review in place.reviews:
            if query.lower() in review.text.lower():
                results.append(place)
                break

    return results