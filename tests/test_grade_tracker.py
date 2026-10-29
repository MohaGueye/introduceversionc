import pytest

from src.grade_tracker import calculate_average, get_letter_grade, is_passing


def test_calculate_average_regular_values():
    assert calculate_average([80, 90, 100]) == 90.0


def test_calculate_average_decimal_values():
    assert calculate_average([72.5, 81.5, 90.0]) == 81.33333333333333


def test_calculate_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_is_passing_threshold():
    assert is_passing(60)
    assert not is_passing(59.9)


def test_get_letter_grade_range():
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(85) == "B"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(50) == "F"
