import allure
from pages.qa_scooter_main_page import MainPage
from pages.qa_scooter_order_page import OrderPage


@allure.title('Проверка  нажатие на scooter_logo')
@allure.description('Проверяем что по нажатие scooter_logo попадёшь на главную страницу «Самоката»')
@allure.step('test_click_scooter_logo')
def test_click_scooter_logo(browser):
    main_page = MainPage(browser)
    order_page = OrderPage(browser)
    main_page.go_to_site()
    main_page.click_on_order_button_on_top()
    order_page.click_on_scooter_logo()
    expected_result = 'https://qa-scooter.praktikum-services.ru/'
    actual_result = main_page.curent_url()
    assert expected_result == actual_result
