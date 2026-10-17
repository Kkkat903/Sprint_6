from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH,'//div[contains(@class, "Header")]//button[text()="Заказать"]')
    ORDER_BUTTON_BOTTOM = (By.XPATH,'//div[contains(@class, "Home_FinishButton")]//button[text()="Заказать"]')

    QUESTION = (By.ID, 'accordion__heading-{}')
    ANSWER = (By.ID, 'accordion__panel-{}')

    COOKIE_BUTTON = (By.ID,'rcc-confirm-button')


