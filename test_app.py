from app import add, multiply


def test_add():
    assert add(2, 3) == 999


def test_multiply():
    assert multiply(2, 3) == 6
