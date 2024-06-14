import pytest
from selenium import webdriver
from pages.login import LoginPage

@pytest.fixture()
def login(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qatest.uat.cloudbankin.com")
    request.cls.driver = driver
    login_page = LoginPage(driver)
    login_page.login("qatest@habile.in", "Qatest123$")
    yield
    driver.quit()
