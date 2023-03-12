from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        return self.driver.get(self.base_url)


    def curent_url(self):
        return self.driver.current_url


    def find_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator),
                                                      message=f"Not find {locator}")

    def find_presence_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Not find {locator}")

    def scroll_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
