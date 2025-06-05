import time
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("invalid_user", "invalid_password")])

def test_login_validate_user(username, password):
    #Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    #Create an instance of the login page
    login_page = LoginPage(driver)

    #Perform Login
    login_page.login(username, password)

    if (username == "standard_user" and password == "secret_sauce") or \
    (username == "problem_user" and password == "secret_sauce"):
        assert "inventory" in driver.current_url
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

        home_page = HomePage(driver)
        home_page.logout()
    else:
        error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_element.is_displayed()

    #Close the browser
    driver.quit()
