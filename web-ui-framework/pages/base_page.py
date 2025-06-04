from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, by_locator):
        """Find an element on the page."""
        return self.driver.find_element(*by_locator)
    
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(by_locator)
        ).click()

    def type(self, by_locator, text):
        """Type text into an input field."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text)

    def get_text(self, by_locator):
        """Get text from an element."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).text
    
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)
    
    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)