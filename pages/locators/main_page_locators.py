from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать' and @class='Button_Button__ra12g']",
    )
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать' and @class='Button_Button__ra12g Button_UltraBig__UU3Lp']",
    )
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")

    FAQ_BUTTONS = (By.XPATH, "//div[@class='accordion__button']")
    FAQ_ANSWERS = (By.XPATH, "//div[@class='accordion__panel']/p")
