from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.CSS_SELECTOR, "input#username")
    __password_locator = (By.CSS_SELECTOR, "input#password")
    __submit_locator = (By.CSS_SELECTOR, "button#submit")
    __success_message = (By.CSS_SELECTOR, ".post-title")
    __logout_button = (By.CSS_SELECTOR, "a.wp-block-button__link")
    __error_message = (By.CSS_SELECTOR, "div#error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_locator, username)
        super()._type(self.__password_locator, password)
        super()._click(self.__submit_locator)
