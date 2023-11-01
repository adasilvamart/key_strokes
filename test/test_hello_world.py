import pytest
from src.key_strokes import key_strokes

@pytest.mark.hello_world
def test_hello_world_dotted():
    assert key_strokes([(5, 1), (2, 0), (8, 1), (8, 1), (8, 0), (8, 2), (5, 3), (1, 0), (8, 0), (3, 0), (8, 1), (2, 1)]) == "Hello. World"

@pytest.mark.hello_world
def test_hello_world():
    assert key_strokes([(5, 1), (2, 0), (8, 1), (8, 1), (8, 0), (5, 3), (1, 0), (8, 0), (3, 0), (8, 1), (2, 1)]) == "Hello world"

