from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()
    
    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)
   