from .base_page import BasePage
from .locators.main_page_locators import MainPageLocators
from .locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class MainPage(BasePage):

    @allure.step("Нажать на верхнюю кнопку заказа")
    def click_top_order_button(self):
        order_button = self.wait_for_clickable(MainPageLocators.TOP_ORDER_BUTTON)
        self.click_element(order_button)
        return self

    @allure.step("Нажать на нижнюю кнопку заказа")
    def click_bottom_order_button(self):
        order_button = self.wait_for_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(order_button)
        return self

    @allure.step("Получить ответ на вопрос FAQ")
    def get_question_answer(self, question_index):
        questions = self.find_elements(MainPageLocators.QUESTION_LOCATOR)

        if question_index >= len(questions):
            raise IndexError(f"Question index {question_index} out of range")

        question = questions[question_index]

        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        self.driver.execute_script("arguments[0].click();", question)

        answer_locator = MainPageLocators.FAQ_ANSWER(question_index)
        answer_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(answer_locator)
        )

        time.sleep(1)

        return answer_element.text

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        yandex_logo = self.wait_for_clickable(BaseLocators.YANDEX_LOGO)
        yandex_logo.click()

        window_handles = self.driver.window_handles

        if len(window_handles) > 1:
            self.driver.switch_to.window(window_handles[1])

            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url != "about:blank"
            )

        return self.driver.current_url

    @allure.step("Принять куки")
    def accept_cookies(self):

        return super().accept_cookies()
