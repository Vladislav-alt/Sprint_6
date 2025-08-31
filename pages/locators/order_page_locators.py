from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    DATE_DELIVERY = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    RENT_TIME = (By.CSS_SELECTOR, "div.Dropdown-root")
    DROPDOWN_OPTION = (By.CSS_SELECTOR, ".Dropdown-option")  
    BLACK_COLOR_CHECKBOX = (By.XPATH, '//input[@id="black"]')
    GREY_COLOR_CHECKBOX = (By.XPATH, '//input[@id="grey"]')

    LIST_STATION = (By.XPATH, '//div[@class="select-search__select"]//button')
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    ORDER_COMPLETED = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')