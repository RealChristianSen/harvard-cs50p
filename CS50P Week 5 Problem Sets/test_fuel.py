import pytest

from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("3/4") == 75


def test_valueerror():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("x/1")
    with pytest.raises(ValueError):
        convert("1/y")
    with pytest.raises(ValueError):
        convert("-1/1")


def test_zerodiverror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
