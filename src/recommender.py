from src.experience_profiles import EXPERIENCE_PROFILES
from src.models import Place


def score_place(
        place: Place,
        experience: str,
) -> int:
    profile = EXPERIENCE_PROFILES.get(experience)

    if profile is None:
        return 0
    
    score = 0

    for tag in profile:
        if tag in place.experience_tags:
            score += 1

    return score