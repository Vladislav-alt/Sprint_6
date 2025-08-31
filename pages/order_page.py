from .base_page import BasePage
from .locators import OrderPageLocators
from utils.urls import Urls
from selenium.webdriver.common.keys import Keys
import allure


class OrderPage(BasePage):

    @allure.step("Открыть страницу заказа")
    def go_to_order_page(self):
        self.open_url(Urls.ORDER_PAGE)
        return self

    @allure.step("Принять куки (если есть)")
    def accept_cookies(self):
        try:
            cookie_btn = self.find_element(OrderPageLocators.COOKIE_BUTTON)
            self.click_element(cookie_btn)
        except:
            pass
        return self

    @allure.step("Ввести имя: {name}")
    def user_name(self, name):
        element = self.find_element(OrderPageLocators.NAME)
        element.clear()
        element.send_keys(name)
        return self

    @allure.step("Ввести фамилию: {last_name}")
    def user_last_name(self, last_name):
        element = self.find_element(OrderPageLocators.LAST_NAME)
        element.clear()
        element.send_keys(last_name)
        return self

    @allure.step("Ввести адрес: {address}")
    def user_address(self, address):
        element = self.find_element(OrderPageLocators.ADDRESS)
        element.clear()
        element.send_keys(address)
        return self

    @allure.step("Выбрать станцию метро: {metro_station}")
    def metro(self, metro_station):
        metro_field = self.find_element(OrderPageLocators.METRO)
        self.click_element(metro_field)
        metro_field.clear()
        metro_field.send_keys(metro_station)
        metro_field.send_keys(Keys.DOWN, Keys.ENTER)
        return self

    @allure.step("Ввести телефон: {phone}")
    def user_phone(self, phone):
        element = self.find_element(OrderPageLocators.NUMBER)
        element.clear()
        element.send_keys(phone)
        return self

    @allure.step("Нажать кнопку 'Далее'")
    def click_button_next(self):
        button = self.find_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(button)
        self.wait_for_visibility(OrderPageLocators.DATE_DELIVERY)
        return self

    @allure.step("Ввести дату доставки: {date}")
    def date_of_delivery(self, date):
        date_field = self.find_element(OrderPageLocators.DATE_DELIVERY)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        return self

    @allure.step("Выбрать период аренды: {period_text}")
    def rental_time(self, period_text):
        rent_dropdown = self.find_element(OrderPageLocators.RENT_TIME)
        self.click_element(rent_dropdown)
        
        first_option = self.find_element(OrderPageLocators.DROPDOWN_OPTION)
        self.click_element(first_option)
        return self

    @allure.step("Выбрать цвет: {color}")
    def checkbox_color(self, color):
        checkbox = self.find_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        self.click_element(checkbox)
        return self

    @allure.step("Ввести комментарий: {comment}")
    def comment_for_courier(self, comment):
        element = self.find_element(OrderPageLocators.COMMENT)
        element.clear()
        element.send_keys(comment)
        return self

    @allure.step("Нажать кнопку 'Заказать'")
    def click_button_order(self):
        order_button = self.find_element(OrderPageLocators.ORDER_BUTTON)
        self.scroll_to_element(order_button)
        self.click_element(order_button)
        self.wait_for_visibility(OrderPageLocators.ORDER_MODAL)
        return self

    @allure.step("Подтвердить заказ")
    def click_button_confirmations(self):
        yes_button = self.find_element(OrderPageLocators.YES_BUTTON)
        self.click_element(yes_button)
        return self

    @allure.step("Проверить окно подтверждения")
    def confirmation_window(self):
        element = self.wait_for_visibility(OrderPageLocators.ORDER_COMPLETED)
        return element

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