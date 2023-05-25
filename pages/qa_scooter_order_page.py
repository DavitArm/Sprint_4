from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QaScooterOrderLocators:

    FIRST_NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADDRESS_TO_BRING_ORDER = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    STATION_METRO = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    THELEPHON = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    CALENDAR = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    MARCH_10 = (By.XPATH, "//div[@aria-label = 'Choose среда, 10-е мая 2023 г.']")
    MARCH_11 = (By.XPATH, "//div[@aria-label = 'Choose четверг, 11-е мая 2023 г.']")
    RENTAL_PERIOD = (By.XPATH, "// div[ @class = 'Dropdown-placeholder']")
    DAY = (By.XPATH, "// div[text() = 'сутки']")
    TWO_DAYS = (By.XPATH, "// div[text() = 'двое суток']")
    SCOOTER_COLOR_BLACK = (By.XPATH, "//input[@id='black']")
    SCOOTER_COLOR_GREY = (By.XPATH, "//input[@id='grey']")
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")
    BUTTON_ORDER_PAGE = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_IS_PROCESSED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class ='Header_LogoScooter__3lsAR']")

    test_data_order = [['Митино', MARCH_10, DAY, SCOOTER_COLOR_BLACK, 'Очень срочно надо'],
                       ['Парк Победы', MARCH_11, TWO_DAYS, SCOOTER_COLOR_GREY, 'Перевозка бесплатно?']]


class OrderPage(BasePage):

    def set_first_name(self, first_name):
        First_name = self.find_element_to_be_clickable(QaScooterOrderLocators.FIRST_NAME)
        First_name.click()
        First_name.send_keys(first_name)
        return First_name

    def set_last_name(self, last_name):
        Last_name = self.find_element_to_be_clickable(QaScooterOrderLocators.LAST_NAME)
        Last_name.click()
        Last_name.send_keys(last_name)
        return Last_name

    def set_address(self, address):
        Address = self.find_element_to_be_clickable(QaScooterOrderLocators.ADDRESS_TO_BRING_ORDER)
        Address.click()
        Address.send_keys(address)
        return Address


    def set_user_data(self, first_name, last_name, address):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)


    def choose_station_metro(self,station_name):
        station_metro = self.find_element_to_be_clickable(QaScooterOrderLocators.STATION_METRO)
        station_metro.click()
        station_metro.send_keys(station_name)
        station_metro.send_keys(Keys.DOWN,Keys.ENTER)


    def set_telephone(self,telephone):
        telle = self.find_element_to_be_clickable(QaScooterOrderLocators.THELEPHON)
        telle.click()
        telle.send_keys(telephone)
        return telle

    def click_on_next_button(self):
        return self.find_element_to_be_clickable(QaScooterOrderLocators.NEXT_BUTTON).click()


    def set_when_to_bring_scooter(self,calendar):
        self.find_element_to_be_clickable(QaScooterOrderLocators.CALENDAR).click()
        return self.find_element_to_be_clickable(calendar).click()


    def set_rental_period(self,day):
        self.find_element_to_be_clickable(QaScooterOrderLocators.RENTAL_PERIOD).click()
        self.find_element_to_be_clickable(day).click()


    def set_scooter_color(self,scooter_color):
        return self.find_element_to_be_clickable(scooter_color).click()


    def set_comment_for_curier(self,com_text):
        comm = self.find_element_to_be_clickable(QaScooterOrderLocators.COMMENT_FOR_COURIER)
        comm.click()
        comm.send_keys(com_text)
        return comm

    def click_on_button_order(self):
        return self.find_element_to_be_clickable(QaScooterOrderLocators.BUTTON_ORDER_PAGE).click()


    def click_on_button_yes(self):
        return self.find_element_to_be_clickable(QaScooterOrderLocators.BUTTON_YES).click()


    def wait_until_view_status_button_text(self):
        return self.find_presence_of_element_located(QaScooterOrderLocators.ORDER_IS_PROCESSED).text


    def click_on_scooter_logo(self):
        return self.find_element_to_be_clickable(QaScooterOrderLocators.SCOOTER_LOGO).click()
