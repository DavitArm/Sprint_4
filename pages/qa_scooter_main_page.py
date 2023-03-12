import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QaScooterMainLocators:

    ORDER_BUTTON_ON_TOP = (By.XPATH, "//Button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BELOW = (By.XPATH, "//Button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    TEXT_QUESTIONS_ABOUT_IMPORTANT = (By.XPATH, "// div[text() = 'Вопросы о важном']")
    QUESTIONS_SECTION_ARROW_1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    QUESTIONS_SECTION_ARROW_2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    QUESTIONS_SECTION_ARROW_3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    QUESTIONS_SECTION_ARROW_4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    QUESTIONS_SECTION_ARROW_5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    QUESTIONS_SECTION_ARROW_6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    QUESTIONS_SECTION_ARROW_7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    QUESTIONS_SECTION_ARROW_8 = (By.XPATH, "//div[@id='accordion__heading-7']")
    RELEVANT_TEXT_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    RELEVANT_TEXT_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    RELEVANT_TEXT_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    RELEVANT_TEXT_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    RELEVANT_TEXT_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    RELEVANT_TEXT_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    RELEVANT_TEXT_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    RELEVANT_TEXT_8 = (By.XPATH, "//div[@id='accordion__panel-7']")
    YANDEX_LOGO = (By.XPATH, "//a[@class ='Header_LogoYandex__3TSOI']")
    YANDEX_LOGO_ROBOT = (By.XPATH, "//a[@class = 'Link Link_view_default LogoLink']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class ='Header_LogoScooter__3lsAR']")
    DZEN_LOGO = (By.XPATH, "//span[@aria-label='Логотип Дзен']")


    test_data_main = [[QUESTIONS_SECTION_ARROW_1,RELEVANT_TEXT_1,'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                      [QUESTIONS_SECTION_ARROW_2,RELEVANT_TEXT_2,'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                      [QUESTIONS_SECTION_ARROW_3,RELEVANT_TEXT_3,'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                      [QUESTIONS_SECTION_ARROW_4,RELEVANT_TEXT_4,'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                      [QUESTIONS_SECTION_ARROW_5,RELEVANT_TEXT_5,'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                      [QUESTIONS_SECTION_ARROW_6,RELEVANT_TEXT_6,'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                      [QUESTIONS_SECTION_ARROW_7,RELEVANT_TEXT_7,'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                      [QUESTIONS_SECTION_ARROW_8,RELEVANT_TEXT_8,'Да, обязательно. Всем самокатов! И Москве, и Московской области.'],]


class MainPage(BasePage):

    def click_on_order_button_on_top(self):
        return self.find_element_to_be_clickable(QaScooterMainLocators.ORDER_BUTTON_ON_TOP).click()


    def click_on_order_button_bellow(self):
        return self.find_element_to_be_clickable(QaScooterMainLocators.ORDER_BUTTON_BELOW).click()


    def scroll_to_order_button_bellow(self):
        element = self.find_presence_of_element_located(QaScooterMainLocators.ORDER_BUTTON_BELOW)
        return self.scroll_to_element(element)


    def scroll_to_text_question_about_important(self):
        element = self.find_presence_of_element_located(QaScooterMainLocators.TEXT_QUESTIONS_ABOUT_IMPORTANT)
        return self.scroll_to_element(element)


    def click_on_question_about_important_arrow(self, important_arrow):
        return self.find_element_to_be_clickable(important_arrow).click()


    def opening_relevant_text(self,texts):
        return self.find_presence_of_element_located(texts).text


    def click_on_yandex_logo(self):
        return self.find_element_to_be_clickable(QaScooterMainLocators.YANDEX_LOGO).click()


    @staticmethod
    def switch_to_new_tab(browser):
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        time.sleep(2)
