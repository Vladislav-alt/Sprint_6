import allure
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from utils.urls import Urls


@allure.epic("Главная страница")
class TestMainPage:

    @allure.feature("FAQ")
    @allure.title("Проверка ответов в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize(
        "question_index,expected_answer",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        ]
    )
    def test_faq_answers(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(question_index)
        
        answers = main_page.find_elements((By.XPATH, "//div[@class='accordion__panel']/p"))
        assert answers[question_index].text == expected_answer

    @allure.feature("Навигация")
    @allure.title("Проверка клика по верхней кнопке 'Заказать'")
    def test_top_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        
        assert "order" in main_page.get_current_url()

    @allure.feature("Навигация")
    @allure.title("Проверка клика по нижней кнопке 'Заказать'")
    def test_bottom_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        
        assert "order" in main_page.get_current_url()

    @allure.feature("Логотипы")
    @allure.title("Проверка: логотип Самоката ведет на главную страницу")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        main_page.click_scooter_logo()
        
        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.feature("Логотипы")
    @allure.title("Проверка: логотип Яндекса открывает новую вкладку")
    def test_yandex_logo_opens_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        
        main_page.switch_to_window(1)
        main_page.wait_url_until_not_about_blank()
        current_url = main_page.get_current_url()
        
        assert any(domain in current_url for domain in ["yandex.ru", "dzen.ru", "ya.ru"])