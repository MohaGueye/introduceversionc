from typing import Iterable


def calculate_average(scores: Iterable[float]) -> float:
    """Return the arithmetic mean of a numeric list of scores."""
    values = list(scores)
    if not values:
        raise ValueError("Scores list cannot be empty.")
    return sum(values) / len(values)


def is_passing(score: float, passing_threshold: float = 60.0) -> bool:
    """Return True when the average meets or exceeds the passing threshold."""
    return score >= passing_threshold


def get_letter_grade(score: float) -> str:
    """Convert a numeric average to a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
