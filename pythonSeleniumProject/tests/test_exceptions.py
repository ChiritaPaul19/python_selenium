import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:
    @pytest.mark.exceptions
    def test_NoSuchElementException(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()
        # Wait for element to be displayed
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # Verify that row2 is displayed
        row2_input = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_input.is_displayed(), "Row 2 is displayed"

    @pytest.mark.exceptions
    def test_secondRowFunctionality(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()
        # Wait for element to be displayed
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # Verify that row2 is displayed
        row2_input = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_input.is_displayed(), "Row 2 is displayed but it is not"
        # Insert text into row2 field
        row2_input.send_keys("Pasta")
        # Click Save button
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        # Check if the message appeared
        confirmation_message = driver.find_element(By.CSS_SELECTOR, "div#confirmation").text
        assert confirmation_message == "Row 2 was added"

    @pytest.mark.exceptions
    def test_clearAndInputNewText(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Find and click Edit button
        edit_button = driver.find_element(By.CSS_SELECTOR, "button#edit_btn")
        edit_button.click()
        # Click on input and change text
        row1_input = driver.find_element(By.CSS_SELECTOR, "input.input-field")
        assert row1_input.is_displayed()
        row1_input.clear()
        row1_input.send_keys("Pasta")
        # Click Save button
        driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']").click()
        confirmation_popup = driver.find_element(By.CSS_SELECTOR, "div#confirmation")
        assert confirmation_popup.is_displayed()

    def test_instructionTabDisappears(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        instruction_tab = driver.find_element(By.CSS_SELECTOR, "p#instructions")
        assert instruction_tab.is_displayed()
        # Add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()
        # Wait for element to be displayed
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # Verify that row2 is displayed
        assert wait.until(ec.invisibility_of_element_located(instruction_tab)), "Row 2 is displayed"

