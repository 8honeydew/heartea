from src.models import Place, Review

places = [
    Place(
        name="Summit Coffee",
        city="Davidson",
        category="coffee",
        experience_tags=[
            "study-friendly",
            "outdoor",
            "remote-work"
        ],
        reviews=[
            Review(author="A", rating=5, text="Great for studying for hours"),
            Review(author="B", rating=4, text="Quiet and good WiFi"),
        ],
    ),
    Place(
        name="Waterbean Coffee",
        city="Cornelius",
        category="coffee",
        experience_tags=[
            "study-friendly",
            "cozy",
            "remote-work"
        ],
        reviews=[
            Review(author="C", rating=5, text="Perfect remote work spot"),
        ],
    ),
    Place(
        name="Mugs Coffee",
        city="Charlotte",
        category="coffee",
        experience_tags=[
            "cozy",
            "quiet",
            "remote-work"
        ],
        reviews=[
            Review(author="E", rating=5, text="The atmosphere of MUGS was suitable and inviting."),
        ],
    ),
    Place(
        name="Main Street Books",
        city="Davidson",
        category="books",
        experience_tags=[
            "study-friendly",
            "quiet",
            "family-friendly"
        ],
        reviews=[
            Review(author="F", rating=4, text="They had a great selection and also offer wrapping as well as some small gifts."),
        ],
    ),
    Place(
        name="Brickhouse Tavern",
        city="Davidson",
        category="restaurant",
        experience_tags=[
            "fast-service",
            "conversation",
            "outdoor"
        ],
        reviews=[
            Review(author="G", rating=1, text="Pizza was greasy and tasted worse than freezer pizza, sauce was tart/sour."),
        ],
    ),
    Place(
        name="Jetton Park",
        city="Cornelius",
        category="park",
        experience_tags=[
            "study-friendly",
            "quiet",
            "family-friendly"
        ],
        reviews=[
            Review(author="H", rating=5, text="Jetton park in Cornelius NC is one of the best and most scenic parks in the area."),
        ],
    ),
]