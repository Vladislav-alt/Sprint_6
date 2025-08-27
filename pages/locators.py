from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    
    QUESTION_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    ANSWER_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")
    
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@href, '/')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex')]")

class OrderPageLocators:
    # Первая страница
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    LIST_STATION = (By.XPATH, "//div[@class='select-search__select']//button")
    NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая страница
    DATE_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    SELECT_RENT_TIME = (By.XPATH, "//div[@class='Dropdown-option' and contains(text(), '{}')]")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    
    ORDER_BUTTON = (By.XPATH, "//button[text()='Назад']/parent::div/button[text()='Заказать']")
    
    # Модальное окно
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_COMPLETED = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")