import time
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("invalid_user", "invalid_password")])

@pytest.mark.smoke
def test_login_validate_user(browser, username, password):
    #Initialize the Chrome driver
    driver = browser
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
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

@pytest.mark.regression
def test_login_invalid_user(browser):
    #Initialize the Chrome driver
    driver = browser
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
    #Create an instance of the login page
    login_page = LoginPage(driver)

    #Perform Login with invalid user
    login_page.login("invalid_user", "invalid_password")

    #Verify error message is displayed
    error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_element.is_displayed()

    #Close the browser
    driver.quit()