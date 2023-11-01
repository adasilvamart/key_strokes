import pytest
from src.key_strokes import key_strokes

@pytest.mark.after_punctuation
def test_after_punct():
    assert key_strokes([(5, 1), (2, 0), (8, 1), (8, 1), (8, 0), (9, 2), (4, 3), (1, 0), (8, 0), (3, 0), (8, 1), (2, 1), (8, 2)])