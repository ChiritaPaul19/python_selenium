from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.CSS_SELECTOR, "input#username")
    __password_locator = (By.CSS_SELECTOR, "input#password")
    __submit_locator = (By.CSS_SELECTOR, "button#submit")
    __success_message = (By.CSS_SELECTOR, ".post-title")
    __logout_button = (By.CSS_SELECTOR, "a.wp-block-button__link")
    __error_message = (By.CSS_SELECTOR, "div#error")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.visibility_of_element_located(self.__username_locator))
        self._driver.find_element(self.__username_locator).send_keys(username)
        wait.until(ec.visibility_of_element_located(self.__password_locator))
        self._driver.find_element(self.__password_locator).send_keys(password)
        wait.until(ec.visibility_of_element_located(self.__submit_locator))
        self._driver.find_element(self.__submit_locator).click()

        current_url = self._driver.current_url

        assert current_url.__contains__("logged-in-successfully")
        assert not current_url.__contains__("logged-out-successfully")
        assert self._driver.find_element(self.__success_message).is_displayed()
        assert self._driver.find_element(self.__logout_button).is_displayed()
