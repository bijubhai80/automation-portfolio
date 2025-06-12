import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager


# def driver():
#     # Initialize the Chrome driver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
    
#     # Maximize the browser window
#     driver.maximize_window()
    
#     # Yield the driver to the test function
#     yield driver
    
#     # Close the browser after the test is done
#     driver.quit()
@pytest.fixture
def browser():
    # Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Yield the driver to the test function
    yield driver
    
    # Close the browser after the test is done
    driver.quit()


def test_login_validatie_user(browser):
    # Navigate to the login page
    browser.get("https://www.saucedemo.com/")
    
    # Find the username and password fields and enter valid credentials
    username_field = browser.find_element("name", "username")
    password_field = browser.find_element("name", "password")
    
    username_field.send_keys("valid_user")
    password_field.send_keys("valid_password")
    
    # Submit the form
    login_button = browser.find_element("name", "login")
    login_button.click()
    
    # Check if the login was successful
    assert "Welcome" in browser.page_source

@pytest.fixture
def browser():
    # Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Yield the driver to the test function
    yield driver
    
    # Close the browser after the test is done
    driver.quit()