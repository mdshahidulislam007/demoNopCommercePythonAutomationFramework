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


#***************** generating pytest HTML reports *************

# hook for adding information into html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce Application'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Shahidul'

#hook for modify/ delete environment into html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins', None)