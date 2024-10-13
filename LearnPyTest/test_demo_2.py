import pytest


def test_m3():
    assert True


@pytest.mark.login
def test_m4():
    assert False


def test_m5():
    assert 100 == 100


def test_login():
    assert "admin" == "admin"


def test_login_Gmail():
    assert "admin" == "admin"
