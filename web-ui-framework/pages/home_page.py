from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)
