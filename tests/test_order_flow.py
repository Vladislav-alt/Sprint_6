import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic("Создание заказа")
class TestOrderFlow:

    @pytest.mark.parametrize("data_set", ["data0", "data1"])
    @allure.title("Полное оформление заказа с данными: {data_set}")
    def test_complete_order_flow(self, driver, data_set):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        test_data = {
            "data0": {
                "user": {
                    "name": "Иван",
                    "last_name": "Иванов",
                    "address": "ул. Пушкина, д. 10",
                    "metro": "Сокольники",
                    "phone": "+79991234567",
                },
                "rent": {
                    "date": "20.12.2024",
                    "period_text": "сутки",
                    "color": "черный",
                    "comment": "Оставить у двери",
                },
            },
            "data1": {
                "user": {
                    "name": "Петр",
                    "last_name": "Петров",
                    "address": "ул. Лермонтова, д. 5",
                    "metro": "Черкизовская",
                    "phone": "+79997654321",
                },
                "rent": {
                    "date": "25.12.2024",
                    "period_text": "двое суток",
                    "color": "серый",
                    "comment": "Позвонить перед выездом",
                },
            },
        }

        main_page.open()
        main_page.accept_cookies()

        customer = test_data[data_set]["user"]
        rental = test_data[data_set]["rent"]

        if data_set == "data0":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        success_element = order_page.user_rent_order(customer, rental)

        assert (
            success_element.is_displayed()
        ), "Элемент подтверждения заказа не отображается"
        assert "Заказ оформлен" in success_element.text
