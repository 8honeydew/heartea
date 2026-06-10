from fastapi import FastAPI, Query
from src.db import places
from src.recommender import score_place

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

@app.get("/tag-search")
def tag_search(tag: str):
    results = []

    for place in places:
        if tag in place.experience_tags:
            results.append(place)

    return results

@app.get("/recommend")
def recommend(experience: str):
    ranked_places = []

    for place in places:
        score = score_place(place, experience)

        if score > 0:
            ranked_places.append(
                {
                    "place": place,
                    "score": score,
                }
            )

    ranked_places.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return ranked_places