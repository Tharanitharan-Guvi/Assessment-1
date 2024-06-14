from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (assuming you have the ChromeDriver in your PATH)
driver = webdriver.Chrome()

try:
    # Step 1: Open the login page
    driver.get("https://qatest.uat.cloudbankin.com")

    # Maximize the window
    driver.maximize_window()

    # Step 2: Log in to the application
    username = driver.find_element(By.XPATH, '//*[@id="uid"]')
    password = driver.find_element(By.XPATH, '//*[@id="pwd"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username.send_keys("qatest@habile.in")
    password.send_keys("Qatest123$")
    login_button.click()

    # Wait for the dashboard to load
    time.sleep(5)  # Adjust the sleep time if necessary

    # Step 3: Locate the navigation bar and print all list items
    nav_items = driver.find_elements(By.XPATH, )

    print("Navigation Bar Items:")
    for item in nav_items:
        print(item.is_enabled())

finally:
    # Close the WebDriver
    driver.quit()
