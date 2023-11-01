import pytest
from src.key_strokes import key_strokes

@pytest.mark.i_by_itself
def test_I_by_itself():
    assert key_strokes([(5, 1), (2, 0), (8, 1), (8, 1), (8, 0), (5, 3), (7, 0), (5, 3), (0, 1), (6, 2)]) == ("Hello I am")

@pytest.mark.i_by_itself
def test_i_followed_by_letter():
    assert key_strokes([(5, 1), (2, 0), (8, 1), (8, 1), (8, 0), (5, 3), (7, 0), (5, 2)]) == ("Hello in")