import pytest


def always_returns_true():
    print("This is going to cause a problem!")
    print("trying this again")
    print("hahaha")
    return True


def test_always_returns_true():
    assert always_returns_true()
