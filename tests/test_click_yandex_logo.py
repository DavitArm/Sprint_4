import allure
from pages.qa_scooter_main_page import MainPage


class TestYandexLogo:
    @allure.title('Проверка  нажатие на yandex_logo')
    @allure.description('Проверяем что по нажатие yandex_logo заказа откриваеться страница yandex')
    @allure.step('test_click_yandex_logo')
    def test_click_yandex_logo(self,browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_yandex_logo()
        main_page.switch_to_new_tab(browser)
        expected_result = 'https://dzen.ru/?yredirect=true'
        actual_result = main_page.curent_url()
        assert expected_result == actual_result

    @allure.title('Проверка  нажатие на yandex_logo из страницы order')
    @allure.description('Проверяем что по нажатие yandex_logo откриваеться страница yandex')
    @allure.step('test_click_yandex_logo_from_order_page')
    def test_click_yandex_logo_from_order_page(self,browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_order_button_on_top()
        main_page.click_on_yandex_logo()
        main_page.switch_to_new_tab(browser)
        expected_result = 'https://dzen.ru/?yredirect=true'
        actual_result = main_page.curent_url()
        assert expected_result == actual_result
