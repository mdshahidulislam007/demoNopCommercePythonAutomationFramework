from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=".\\Drivers\\chromedriver.exe")
        print("*********** Launching Chrome Browser ************")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=".\\Drivers\\geckodriver.exe")
        print("*********** Launching Firefox Browser ************")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
