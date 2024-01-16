import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_login_username(self, driver):
        # Go to link
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Insert username
        username_locator = driver.find_element(By.CSS_SELECTOR, "input#username")
        username_locator.send_keys("incorrectUser")

        # Insert password
        password_locator = driver.find_element(By.CSS_SELECTOR, "input#password")
        password_locator.send_keys("Password123")

        # Press submit
        submit_locator = driver.find_element(By.CSS_SELECTOR, "button#submit")
        submit_locator.click()
        time.sleep(1)

        # Verify that user remained on the same page
        error_message = driver.find_element(By.ID, "error")
        current_url = driver.current_url

        assert current_url.__contains__("practice-test-login")
        assert not current_url.__contains__("logged-in-successfully")
        assert error_message.is_displayed()

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_login_password(self, driver):
        # Go to link
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Insert username
        username_locator = driver.find_element(By.CSS_SELECTOR, "input#username")
        username_locator.send_keys("student")

        # Insert password
        password_locator = driver.find_element(By.CSS_SELECTOR, "input#password")
        password_locator.send_keys("WrongPassword")

        # Press submit
        submit_locator = driver.find_element(By.CSS_SELECTOR, "button#submit")
        submit_locator.click()
        time.sleep(1)

        # Verify that user remained on the same page
        error_message = driver.find_element(By.CSS_SELECTOR, "div#error")
        current_url = driver.current_url

        assert current_url.__contains__("practice-test-login")
        assert not current_url.__contains__("logged-in-successfully")
        assert error_message.is_displayed()
