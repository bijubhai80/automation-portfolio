from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def validate_home_page(self):
        #Check title is correct
        # assert self.driver.find(By.CLASS_NAME, "title").text == "Products", "Home Page title is incorrect"
        assert self.get_text((By.CLASS_NAME, "title")) == "Products", "Home Page title is incorrect"

        assert self.is_visible(self.menu_button), "Menu button is not visible"


    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)
