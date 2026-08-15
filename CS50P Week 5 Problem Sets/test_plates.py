import pytest

from plates import is_valid


def test_len():
    assert is_valid("plate") == True
    assert is_valid("plateplate") == False
    assert is_valid("plate1") == True


def test_isdigit():
    assert is_valid("10") == False


def test_0():
    assert is_valid("test02") == False
    assert is_valid("0plate") == False


def test_numbers():
    assert is_valid("plate0x") == False
    assert is_valid("pl8t3") == False
    assert is_valid("1000") == False


def test_punctuation():
    assert is_valid(".") == False


def test_non_alphanumerics():
    assert is_valid("test/") == False
