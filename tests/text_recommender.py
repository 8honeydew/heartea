from src.db import places
from src.recommender import score_place


def test_study_score():
    score = score_place(
        places[0],
        "study",
    )

    assert score > 0