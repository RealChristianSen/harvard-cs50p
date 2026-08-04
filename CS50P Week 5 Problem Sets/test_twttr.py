import pytest

from twttr import shorten

def test_vowel_replacement():
    assert shorten("aeiou") == ""

def test_low_vow_repl():
    assert shorten("test") == "tst"

def test_cap_vowel_replacement():
    assert shorten("TEST") == "TST"

def test_omit_int():
    assert shorten("1test") == "1tst"

def test_omit_punctuation():
    assert shorten("test.") == "tst."
