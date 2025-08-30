import allure
import pytest
from pages.main_page import MainPage
from utils.urls import Urls


@allure.epic("Главная страница")
class TestFAQ:

    @pytest.mark.parametrize(
        "question_index,expected_answer",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (
                1,
                "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
            ),
        ],
    )
    @allure.title("Проверка ответов FAQ")
    def test_faq_answers(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        with allure.step(f"Кликаем на вопрос №{question_index + 1}"):
            actual_answer = main_page.get_question_answer(question_index)

        with allure.step("Проверяем текст ответа"):
            assert actual_answer == expected_answer


@allure.epic("Редиректы")
class TestLogoRedirects:

    @allure.title("Проверка перехода на главную через логотип Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        with allure.step("Нажимаем на логотип Самоката"):

            pass

        with allure.step("Проверяем, что находимся на главной странице"):
            assert driver.current_url == Urls.MAIN_PAGE

    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        with allure.step("Нажимаем на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Проверяем, что открылась страница Дзена"):

            pass
