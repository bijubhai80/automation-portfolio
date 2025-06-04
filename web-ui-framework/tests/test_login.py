import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_validate_user():
    #Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    #Create an instance of the login page
    login_page = LoginPage(driver)

    #Perform Login
    login_page.login("standard_user", "secret_sauce")

    #Validate successful login by checking the URL
    assert "inventory" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    #Logout after successful login
    home_page = HomePage(driver)
    home_page.logout()

    #Validate successful logout by checking the URL
    assert "saucedemo.com" in driver.current_url
    #assert "login" in driver.page_source.lower()

    #Close the browser
    driver.quit()
