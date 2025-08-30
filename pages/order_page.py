from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .locators import OrderPageLocators
import allure


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть страницу заказа")
    def go_to_order_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        return self

    @allure.step("Принять куки (если есть)")
    def accept_cookies(self):
        try:
            cookie_btn = self.driver.find_element(By.ID, "rcc-confirm-button")
            cookie_btn.click()
        except:
            pass
        return self

    @allure.step("Ввести имя: {name}")
    def user_name(self, name):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NAME))
        element.clear()
        element.send_keys(name)
        return self

    @allure.step("Ввести фамилию: {last_name}")
    def user_last_name(self, last_name):
        element = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.LAST_NAME)
        )
        element.clear()
        element.send_keys(last_name)
        return self

    @allure.step("Ввести адрес: {address}")
    def user_address(self, address):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ADDRESS))
        element.clear()
        element.send_keys(address)
        return self

    @allure.step("Выбрать станцию метро: {metro_station}")
    def metro(self, metro_station):
        metro_field = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.METRO)
        )
        metro_field.click()
        metro_field.clear()
        metro_field.send_keys(metro_station)

        metro_field.send_keys(Keys.DOWN, Keys.ENTER)
        return self

    @allure.step("Ввести телефон: {phone}")
    def user_phone(self, phone):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NUMBER))
        element.clear()
        element.send_keys(phone)
        return self

    @allure.step("Нажать кнопку 'Далее'")
    def click_button_next(self):
        button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)
        )
        button.click()

        self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_DELIVERY)
        )
        return self

    @allure.step("Ввести дату доставки: {date}")
    def date_of_delivery(self, date):
        date_field = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.DATE_DELIVERY)
        )
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        return self

    @allure.step("Выбрать период аренды: {period_text}")
    def rental_time(self, period_text):
        rent_dropdown = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.RENT_TIME)
        )
        rent_dropdown.click()

        first_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='Dropdown-option'][1]"))
        )
        first_option.click()
        return self

    @allure.step("Выбрать цвет: {color}")
    def checkbox_color(self, color):

        checkbox = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        )
        checkbox.click()
        return self

    @allure.step("Ввести комментарий: {comment}")
    def comment_for_courier(self, comment):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COMMENT))
        element.clear()
        element.send_keys(comment)
        return self

    @allure.step("Нажать кнопку 'Заказать'")
    def click_button_order(self):
        order_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        self.wait.until(EC.visibility_of(order_button))

        order_button.click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
            )
        )
        return self

    @allure.step("Подтвердить заказ")
    def click_button_confirmations(self):

        yes_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.YES_BUTTON)
        )
        yes_button.click()
        return self

    @allure.step("Проверить окно подтверждения")
    def confirmation_window(self):
        element = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED)
        )
        text = element.text
        assert "Заказ оформлен" in text
        return text

    @allure.step("Заполнить данные пользователя")
    def fill_user_data(self, user_data):
        self.user_name(user_data["name"])
        self.user_last_name(user_data["last_name"])
        self.user_address(user_data["address"])
        self.metro(user_data["metro"])
        self.user_phone(user_data["phone"])
        return self

    @allure.step("Заполнить данные аренды")
    def fill_rent_data(self, rent_data):
        self.date_of_delivery(rent_data["date"])
        self.rental_time(rent_data["period_text"])
        self.checkbox_color(rent_data["color"])
        self.comment_for_courier(rent_data["comment"])
        return self

    @allure.step("Выполнить полный сценарий заказа")
    def user_rent_order(self, user_data, rent_data):
        self.go_to_order_page()
        self.accept_cookies()

        self.fill_user_data(user_data)
        self.click_button_next()
        self.fill_rent_data(rent_data)
        self.click_button_order()
        self.click_button_confirmations()
        return self.confirmation_window()
