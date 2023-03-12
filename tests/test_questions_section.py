import allure
import pytest
from pages.qa_scooter_main_page import MainPage, QaScooterMainLocators


@allure.title('Проверка  нажатие на стрелку click_on_question_about_important_arrow ')
@allure.description('Проверяем что по нажатие click_on_question_about_important_arrow откриваеться relevant_text')
@allure.step('test_dropdown_list_important_questions_section')
@pytest.mark.parametrize('important_arrow, opening_text, expected_text', QaScooterMainLocators.test_data_main)
def test_dropdown_list_important_questions_section(browser, important_arrow, opening_text, expected_text):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.scroll_to_text_question_about_important()
    main_page.click_on_question_about_important_arrow(important_arrow)
    expected_result = expected_text
    actually_result = main_page.opening_relevant_text(opening_text)
    assert expected_result == actually_result
