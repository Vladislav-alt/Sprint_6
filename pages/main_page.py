from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  # Добавьте этот импорт
from .locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def accept_cookies(self):
        try:
            cookie_btn = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)
            )
            cookie_btn.click()
        except:
            pass

    def click_order_button(self, button_type="top"):
        if button_type == "top":
            locator = MainPageLocators.ORDER_BUTTON_TOP
        else:
            locator = MainPageLocators.ORDER_BUTTON_BOTTOM

            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script("arguments[0].click();", element)

    def get_question_answer(self, question_index):
        questions = self.wait.until(
            EC.visibility_of_all_elements_located(MainPageLocators.QUESTION_LOCATOR)
        )

        if question_index >= len(questions):
            raise IndexError(f"Question index {question_index} out of range")

        question = questions[question_index]

        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        self.driver.execute_script("arguments[0].click();", question)

        answer_locator = (
            By.XPATH,
            f"//div[@id='accordion__panel-{question_index}' and not(@hidden)]",
        )
        self.wait.until(EC.visibility_of_element_located(answer_locator))

        answer = self.driver.find_element(By.ID, f"accordion__panel-{question_index}")
        return answer.text if answer else None

    def click_scooter_logo(self):
        element = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_yandex_logo(self):
        current_window = self.driver.current_window_handle
        element = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        self.driver.execute_script("arguments[0].click();", element)

        self.wait.until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

        self.wait.until(EC.url_contains("dzen.ru"))
        return self.driver.current_url
