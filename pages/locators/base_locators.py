from selenium.webdriver.common.by import By

class BaseLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@href, '/')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex')]")