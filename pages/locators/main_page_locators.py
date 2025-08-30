from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    QUESTION_LOCATOR = (By.XPATH, ".//div[@class='accordion__button']")
    ANSWER_LOCATOR = (By.CSS_SELECTOR, ".accordion__panel > p")
    
    @staticmethod
    def FAQ_ANSWER(answer_number):
        return (By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p")