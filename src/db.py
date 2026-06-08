from src.models import Place, Review

places = [
    Place(
        name="Summit Coffee",
        city="Davidson",
        category="coffee",
        reviews=[
            Review(author="A", rating=5, text="Great for studying for hours"),
            Review(author="B", rating=4, text="Quiet and good WiFi"),
        ],
    ),
    Place(
        name="Waterbean Coffee",
        city="Cornelius",
        category="coffee",
        reviews=[
            Review(author="C", rating=5, text="Perfect remote work spot"),
        ],
    ),
    Place(
        name="Mugs Coffee",
        city="Charlotte",
        category="coffee",
        reviews=[
            Review(author="E", rating=5, text="The atmosphere of MUGS was suitable and inviting."),
        ],
    ),
    Place(
        name="Main Street Books",
        city="Davidson",
        category="books",
        reviews=[
            Review(author="F", rating=4, text="They had a great selection and also offer wrapping as well as some small gifts."),
        ],
    ),
    Place(
        name="Brickhouse Tavern",
        city="Davidson",
        category="restaurant",
        reviews=[
            Review(author="G", rating=1, text="Pizza was greasy and tasted worse than freezer pizza, sauce was tart/sour."),
        ],
    ),
    Place(
        name="Jetton Park",
        city="Cornelius",
        category="park",
        reviews=[
            Review(author="H", rating=5, text="Jetton park in Cornelius NC is one of the best and most scenic parks in the area."),
        ],
    ),
]