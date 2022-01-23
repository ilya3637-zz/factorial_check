from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-test.emcd.io/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class Locators:
    input_field = (By.XPATH, '//*[@id="number"]')
    button = (By.XPATH, '//*[@id="getFactorial"]')
    result = (By.XPATH, '//*[@id="resultDiv"]')


class MainPage(BasePage):

    def click(self):
        button = self.find_element(Locators.button)
        button.click()

    def input_value(self, value):
        input_field = self.find_element(Locators.input_field)
        input_field.send_keys(value)

    def get_input_value(self):
        input_field = self.find_element(Locators.input_field)
        return input_field.get_attribute('innerHTML')

    def get_result_value(self):
        result = self.find_element(Locators.result)
        return result.get_attribute('innerHTML')
