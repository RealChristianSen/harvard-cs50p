import pytest

from bank import value

def test_value():
    assert value("h") == 20

def test_newman():
    assert value("hello, newman") == 0

def test_hello():
    assert value("hello") == 0

def test_case_insensitivity():
    assert value("H") == 20
    assert value("Hello") == 0
