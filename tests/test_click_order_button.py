import allure
from pages.qa_scooter_main_page import MainPage
from pages.qa_scooter_order_page import OrderPage


class TestClickOrderButton:
    @allure.title('Проверка  нажатие на кнопку order_button_on_top')
    @allure.description('Проверяем что по нажатие кнопку order_button_on_top откриваеться страница order')
    @allure.step('click_on_order_button_on_top')
    def test_click_on_order_button_on_top(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        main_page.go_to_site()
        main_page.click_on_order_button_on_top()
        expected_result = 'https://qa-scooter.praktikum-services.ru/order'
        actually_result = order_page.curent_url()
        assert expected_result == actually_result


    @allure.title('Проверка  нажатие на кнопку order_button_bellow')
    @allure.description('Проверяем что по нажатие кнопку order_button_bellow откриваеться страница order')
    @allure.step('click_on_order_button_bellow')
    def test_click_on_order_button_bellow(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        main_page.go_to_site()
        main_page.scroll_to_order_button_bellow()
        main_page.click_on_order_button_bellow()
        expected_result = 'https://qa-scooter.praktikum-services.ru/order'
        actually_result = order_page.curent_url()
        assert expected_result == actually_result
