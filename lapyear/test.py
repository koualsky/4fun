import pytest
from lapyear import lapyear


def test_1():
    assert lapyear(6) == True


def test_2():
    assert lapyear(5) == False
