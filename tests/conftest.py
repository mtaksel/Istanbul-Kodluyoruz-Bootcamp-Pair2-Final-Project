  

import getpass
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.safari.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest

from pages.constants.globalConstants import *


@pytest.fixture(scope="function")
def setup(request, browser, environment):

    if browser is None:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "safari": #bu projede safari kullanilmadi, ornek icin konuldu
            service = Service("./drivers/safari")
            driver = webdriver.Chrome(service=service)
        else:
            print("Girdiginiz Browser Hatali!!")

    if environment is None:
        base_url = BASE_URL 
    else:
        if environment == "dev":
            base_url = "https://dev-tobeto.com"
        elif environment == "qa":
            base_url = "https://qa-tobeto.com"
        elif environment == "pre-prod":
            base_url = "https://preprod-tobeto.com"
        elif environment == "prod":
            base_url = BASE_URL
        else:
            print("Girdiginiz Environment Hatali!!")

    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.baseurl = base_url
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def environment(request):
    return request.config.getoption("--env")
    
