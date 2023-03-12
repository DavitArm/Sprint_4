import allure
import pytest
from pages.qa_scooter_main_page import MainPage
from pages.qa_scooter_order_page import OrderPage, QaScooterOrderLocators


@pytest.mark.parametrize('station, calendar, day, scooter_color, com_text', QaScooterOrderLocators.test_data_order)
class TestOrder:
    @allure.title('Проверка Заказ самоката нажатие на кнопку order_button_on_top')
    @allure.description('Проверяем что после заказа появилось всплывающее окно с сообщением Заказ оформлен')
    @allure.step('test_order_by_button_top')
    def test_order_by_button_top(self,browser,name,last_name,address,phone,station,calendar,day,scooter_color,com_text):
        order_page = OrderPage(browser)
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_order_button_on_top()
        order_page.set_user_data(name, last_name, address)
        order_page.choose_station_metro(station)
        order_page.set_telephone(phone)
        order_page.click_on_next_button()
        order_page.set_when_to_bring_scooter(calendar)
        order_page.set_rental_period(day)
        order_page.set_scooter_color(scooter_color)
        order_page.set_comment_for_curier(com_text)
        order_page.click_on_button_order()
        order_page.click_on_button_yes()
        expected_result = 'Заказ оформлен'
        actual_result = order_page.wait_until_view_status_button_text()
        assert expected_result in actual_result

    @allure.title('Проверка Заказ самоката нажатие на кнопку order_button_bellow')
    @allure.description('Проверяем что после заказа появилось всплывающее окно с сообщением Заказ оформлен')
    @allure.step('test_order_by_button_top')
    def test_order_by_button_below(self,browser,name,last_name,address,phone,station,calendar,day,scooter_color,com_text):
        order_page = OrderPage(browser)
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.scroll_to_order_button_bellow()
        main_page.click_on_order_button_bellow()
        order_page.set_user_data(name, last_name, address)
        order_page.choose_station_metro(station)
        order_page.set_telephone(phone)
        order_page.click_on_next_button()
        order_page.set_when_to_bring_scooter(calendar)
        order_page.set_rental_period(day)
        order_page.set_scooter_color(scooter_color)
        order_page.set_comment_for_curier(com_text)
        order_page.click_on_button_order()
        order_page.click_on_button_yes()
        expected_result = 'Заказ оформлен'
        actual_result = order_page.wait_until_view_status_button_text()
        assert expected_result in actual_result
