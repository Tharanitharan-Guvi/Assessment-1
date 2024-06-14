import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import LoginPage

@pytest.fixture()
def driver_setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qatest.uat.cloudbankin.com")
    login_page = LoginPage(driver)
    login_page.login("qatest@habile.in", "Qatest123$")
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver_setup")
class TestURLs:
    def test_clients_urls(self, driver_setup):
        # Verify URLs in the Clients dropdown menu
        clients_menu = driver_setup.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[1]/a")
        clients_menu.click()
        clients_links = driver_setup.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[1]/ul/li/a")
        for link in clients_links:
            assert link.get_attribute("href") != "", f"URL {link.text} is empty!"

    def test_accounting_urls(self, driver_setup):
        # Verify URLs in the Accounting dropdown menu
        accounting_menu = driver_setup.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[2]/a")
        accounting_menu.click()
        accounting_links = driver_setup.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[2]/ul/li/a")
        for link in accounting_links:
            assert link.get_attribute("href") != "", f"URL {link.text} is empty!"

    def test_reports_urls(self, driver_setup):
        # Verify URLs in the Reports dropdown menu
        reports_menu = driver_setup.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[3]/a")
        reports_menu.click()
        reports_links = driver_setup.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[3]/ul/li/a")
        for link in reports_links:
            assert link.get_attribute("href") != "", f"URL {link.text} is empty!"

    def test_admin_urls(self, driver_setup):
        # Verify URLs in the Admin dropdown menu
        admin_menu = driver_setup.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[4]/a")
        admin_menu.click()
        admin_links = driver_setup.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/nav/div/div/ul/li[4]/ul/li/a")
        for link in admin_links:
            assert link.get_attribute("href") != "", f"URL {link.text} is empty!"
