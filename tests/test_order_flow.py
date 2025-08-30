import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.data import TestData


class TestOrderFlow:

    @allure.epic("Заказ самоката")
    @allure.feature("Полный флоу заказа")
    @allure.story("Заказ через верхнюю и нижнюю кнопки")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Полный флоу заказа через {button_type} кнопку")  # ← ИСПРАВЛЕНО!
    @allure.description(
        "Тестирование полного процесса заказа самоката через разные кнопки на сайте"
    )
    @pytest.mark.parametrize("data", TestData.get_order_combinations())
    def test_complete_order_flow(self, driver, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()

        customers = TestData.get_valid_customers()
        rentals = TestData.get_rental_data()

        customer = customers[data["customer_index"]]
        rental = rentals[data["rental_index"]]

        button_type = data["button_type"]

        with allure.step("Нажимаем кнопку заказа"):
         if data["button_type"] == "top":
          main_page.click_top_order_button()  
         else:
          main_page.click_bottom_order_button()  

        with allure.step("Выполняем полный сценарий заказа"):
            success_text = order_page.user_rent_order(customer, rental)
            assert "Заказ оформлен" in success_text