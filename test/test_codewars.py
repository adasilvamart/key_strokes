import pytest
from src.key_strokes import key_strokes

@pytest.mark.i_in_quotes
def test_I_can():
    assert key_strokes([(5, 2), (8, 0), (1, 0), (4, 3), (1, 1), (0, 1), (5, 0), (6, 3), (10, 1), (7, 0), (4, 3), (2, 2), (0, 1), (5, 2), (10, 1)]) == ("Now say 'I can'")

@pytest.mark.i_last_upper
def test_yoda():
    assert key_strokes([(5, 0), (8, 0), (2, 1), (0, 1), (7, 2), (5, 3), (0, 1), (6, 2), (4, 3), (7, 0)]) == ("Yoda, am I")