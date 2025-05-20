import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
@pytest.fixture()
def set_up(browser):
    if browser=='chrome':
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser=='edge':
        from selenium.webdriver.edge.service import Service
        serv_obj = Service(r"D:\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

### executing with CLI
## py.test .\test_command_code.py -v -s --browser="chrome"
## py.test .\test_command_code.py -v -s --browser="edge"

