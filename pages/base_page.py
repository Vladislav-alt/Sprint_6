import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перейти по URL")
    def open_url(self, url):
        self.driver.get(url)
        return self

    @allure.step("Кликнуть по элементу")
    def click_element(self, element):
        element.click()
        return self

    @allure.step("Ввести текст в поле")
    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Проверить, что элемент отображается")
    def is_element_displayed(self, element):
        return element.is_displayed()

    @allure.step("Получить текст элемента")
    def get_element_text(self, element):
        return element.text
    
    @allure.step('Дождаться видимости элемента')
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Дождаться, что URL содержит текст')
    def wait_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
        return self

    @allure.step('Дождаться, что URL не about:blank')
    def wait_url_not_about_blank(self, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            EC.url_to_be('about:blank')
        )
        return self

    @allure.step('Подождать секунду')
    def wait_a_second(self):
        import time
        time.sleep(1)
        return self
    
    @allure.step('Скролл к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self

    @allure.step('Скролл наверх страницы')
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        return self

    @allure.step('Скролл вниз страницы')
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self