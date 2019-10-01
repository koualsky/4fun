import pytest
from leapyear import leapyear


def test_400():
    assert leapyear(400) == True


def test_100():
    assert leapyear(100) == False


def test_4():
    assert leapyear(4) == True
