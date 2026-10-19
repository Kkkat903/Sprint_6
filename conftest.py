import pytest
from selenium import webdriver
from urls import Url as U

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(U.BASE_URL)

    yield driver

    driver.quit()