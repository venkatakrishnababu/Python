import pytest
from python_files.decor_main import unchanged_name
from selenium import webdriver
from selenium.webdriver.common.by import By

def testlogin():
    print('login is successful')


def testing1():
    assert unchanged_name("RAHU") == "rahu"


def testing2():
    assert unchanged_name("rahul") == "RAHUL"

@pytest.mark.xfail
def testlogout():
    print('logout is sucessful')


@pytest.mark.parametrize("name, expected", [("rahul", "RAHUL"), ("RAHUL", "rahul")])
def test_param(name, expected):
    assert unchanged_name(name) == expected
