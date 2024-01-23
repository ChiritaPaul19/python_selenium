import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Go to link
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Insert username
        username_locator = driver.find_element(By.CSS_SELECTOR, "input#username")
        username_locator.send_keys("student")

        # Insert password
        password_locator = driver.find_element(By.CSS_SELECTOR, "input#password")
        password_locator.send_keys("Password123")

        # Press submit
        submit_locator = driver.find_element(By.CSS_SELECTOR, "button#submit")
        submit_locator.click()

        # Verify that user is redirected
        success_message = driver.find_element(By.CSS_SELECTOR, ".post-title")
        current_url = driver.current_url
        logout_button = driver.find_element(By.CSS_SELECTOR, "a.wp-block-button__link")

        assert current_url.__contains__("logged-in-successfully")
        assert not current_url.__contains__("logged-out-successfully")
        assert success_message._is_displayed()
        assert logout_button._is_displayed()
