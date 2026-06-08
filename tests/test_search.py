from src.db import places


def test_places_exist():
    assert len(places) > 0