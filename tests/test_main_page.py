import pytest
import allure
from pages.main_page import MainPage
from utils.data import FAQData
from utils.urls import Urls

class TestFAQ:
    
    @allure.title("Проверка ответов в FAQ для вопроса {question_index}")
    @pytest.mark.parametrize("question_index, expected_answer", 
                            FAQData.get_questions_and_answers())
    def test_faq_question_should_show_correct_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step(f"Кликаем на вопрос №{question_index + 1}"):
            actual_answer = main_page.get_question_answer(question_index)
        
        with allure.step("Проверяем текст ответа"):
            assert actual_answer == expected_answer, \
                f"Ожидался: '{expected_answer}', получен: '{actual_answer}'"

class TestLogoRedirects:
    
    @allure.title("Проверка перехода на главную через логотип Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Нажимаем на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем, что находимся на главной странице"):
            assert driver.current_url == Urls.MAIN_PAGE
    
    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Нажимаем на логотип Яндекса"):
            new_url = main_page.click_yandex_logo()
        
        with allure.step("Проверяем, что открылась страница Дзена"):
            assert "dzen.ru" in new_url, f"Expected dzen.ru in URL, but got: {new_url}"
            
        with allure.step("Закрываем вкладку Дзена и возвращаемся"):
            driver.close()
            driver.switch_to.window(driver.window_handles[0])