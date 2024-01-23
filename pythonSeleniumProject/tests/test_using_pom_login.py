import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.pom
    def test_positive_login_using_pom(self, driver):
        login_page = LoginPage(driver)
        # Open page
        login_page.open()
        # Fill username, password and hit submit
        login_page.execute_login("student", "Password123")

        logged_in_successfully = LoggedInSuccessfullyPage(driver)
        assert logged_in_successfully.expected_url == logged_in_successfully.current_url, ("Actual URL is not the same "
                                                                                           "as expected")
        assert logged_in_successfully.header == "Logged In Successfully", "Header not as expected"
        assert logged_in_successfully.is_logout_button_displayed(), "Log out button should be visible"

