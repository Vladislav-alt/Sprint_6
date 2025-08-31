from .base_page import BasePage
from .locators.main_page_locators import MainPageLocators
from utils.urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Urls.MAIN_PAGE)
        return self
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            cookie_btn = self.find_element(MainPageLocators.COOKIE_BUTTON)
            cookie_btn.click()
        except:
            pass
        return self

    @allure.step("Нажать на вопрос FAQ")
    def click_faq_question(self, question_number):
        questions = self.find_elements(MainPageLocators.FAQ_BUTTONS)
        questions[question_number].click()
        return self

    @allure.step("Получить ответ FAQ")
    def get_faq_answer(self, answer_number):
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        return answers[answer_number].text

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        order_btn = self.find_element(MainPageLocators.TOP_ORDER_BUTTON)
        order_btn.click()
        return self

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        order_btn = self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        order_btn.click()
        return self

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        logo = self.find_element(MainPageLocators.SCOOTER_LOGO)
        logo.click()
        return self

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        logo = self.find_element(MainPageLocators.YANDEX_LOGO)
        logo.click()
        return self

    @allure.step("Переключиться на вкладку")
    def switch_to_window(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])
        return self

    @allure.step("Дождаться загрузки страницы")
    def wait_url_until_not_about_blank(self, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            EC.url_to_be('about:blank')
        )
        return self