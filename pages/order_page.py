from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .locators import OrderPageLocators
import time


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def user_name(self, name):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NAME))
        element.clear()
        element.send_keys(name)
        return self

    def user_last_name(self, last_name):
        element = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.LAST_NAME)
        )
        element.clear()
        element.send_keys(last_name)
        return self

    def user_address(self, address):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ADDRESS))
        element.clear()
        element.send_keys(address)
        return self

    def metro(self, metro_station):
        metro_field = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.METRO)
        )
        metro_field.click()
        metro_field.send_keys(metro_station)

        time.sleep(1)
        try:
            station = self.wait.until(
                EC.element_to_be_clickable(OrderPageLocators.LIST_STATION)
            )
            station.click()
        except:
            metro_field.send_keys(Keys.ENTER)
        return self

    def user_phone(self, phone):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NUMBER))
        element.clear()
        element.send_keys(phone)
        return self

    def click_button_next(self):
        button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)
        )
        button.click()
        self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_DELIVERY)
        )
        return self

    def date_of_delivery(self, date):
        date_field = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.DATE_DELIVERY)
        )
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        return self

    def rental_time(self, period_text):
        rent_dropdown = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.RENT_TIME)
        )
        rent_dropdown.click()

        option_locator = (
            By.XPATH,
            f"//div[@class='Dropdown-option' and contains(text(), '{period_text}')]",
        )
        try:
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            option.click()
        except:
            first_option = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='Dropdown-option'][1]")
                )
            )
            first_option.click()
        return self

    def checkbox_color(self, color):
        if color.lower() in ["black", "чёрный", "черный"]:
            checkbox = self.wait.until(
                EC.element_to_be_clickable(OrderPageLocators.BLACK_COLOR_CHECKBOX)
            )
            if not checkbox.is_selected():
                checkbox.click()
        elif color.lower() in ["grey", "серый", "gray"]:
            checkbox = self.wait.until(
                EC.element_to_be_clickable(OrderPageLocators.GREY_COLOR_CHECKBOX)
            )
            if not checkbox.is_selected():
                checkbox.click()
        return self

    def comment_for_courier(self, comment):
        element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COMMENT))
        element.clear()
        element.send_keys(comment)
        return self

    def click_button_order(self):

        order_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)

        print(f"Кнопка активна: {order_button.is_enabled()}")
        print(f"Классы кнопки: {order_button.get_attribute('class')}")

        if not order_button.is_enabled():
            raise Exception(
                "Кнопка 'Заказать' заблокирована! Проверьте заполнение полей."
            )

        order_button.click()
        return self

    def click_button_confirmations(self):
        yes_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.YES_BUTTON)
        )
        yes_button.click()
        return self

    def confirmation_window(self):
        element = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED)
        )
        text = element.text
        assert "Заказ оформлен" in text
        return text

    def fill_user_data(self, user_data):

        self.user_name(user_data["name"])
        self.user_last_name(user_data["last_name"])
        self.user_address(user_data["address"])
        self.metro(user_data["metro"])
        self.user_phone(user_data["phone"])
        return self

    def fill_rent_data(self, rent_data):

        self.date_of_delivery(rent_data["date"])
        self.rental_time(rent_data["period_text"])
        self.checkbox_color(rent_data["color"])
        self.comment_for_courier(rent_data["comment"])
        return self

    def user_rent_order(self, user_data, rent_data):

        self.fill_user_data(user_data)
        self.click_button_next()
        self.fill_rent_data(rent_data)
        self.click_button_order()
        self.click_button_confirmations()
        return self.confirmation_window()
