from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME = (By.XPATH,'//input[@placeholder="* Имя"]')
    LAST_NAME = (By.XPATH,'//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH,'//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_BUTTON = (By.CLASS_NAME, "select-search__input")
    LIST_OF_METRO = (By.XPATH, "//li/button[@value='{}']")
    PHONE_NUMBER = (By.XPATH,'//input[@placeholder="* Телефон: на него позвонит курьер"]')
    
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_RENT = (By.XPATH,"//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENT_OPTION = (By.XPATH,"//div[contains(@class, 'Dropdown-option') and normalize-space(.)='{}']")
    COLOR_SELECT = (By.ID,'{}')
    COMMENT = (By.XPATH,'//input[@placeholder="Комментарий для курьера"]')
   
    ORDER_BUTTON = (By.XPATH,'//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')

    YES_BUTTON = (By.XPATH,'//div[contains(@class, "Order_Buttons__1xGrp")]//button[text()="Да"]')
    ORDER_SUCCESS_MESSAGE = (By.XPATH,'//div[contains(@class, "Order_ModalHeader")][contains(., "Заказ оформлен")]')
    
    SHOW_STATUS_BUTTON = (By.XPATH,'//button[text()="Посмотреть статус"]')
    
    SCOOTER_LOGO = (By.CLASS_NAME,'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME,'Header_LogoYandex__3TSOI')
    