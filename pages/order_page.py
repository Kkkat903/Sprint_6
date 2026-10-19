import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators as O
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):

    @allure.step("Ввести имя")
    def set_name(self,name):
        self.type_text(O.FIRST_NAME,name)

    @allure.step("Ввести фамилию")
    def set_surname(self,surname):
        self.type_text(O.LAST_NAME,surname)

    @allure.step("Внести адрес")
    def set_address(self,address):
        self.type_text(O.ADDRESS,address)

    @allure.step("Открыть выпадающий список станций метро")
    def click_metro(self):
        self.click(O.METRO_BUTTON)

    @allure.step("Выбрать станцию метро")
    def select_metro(self, station):
        locator = self.get_locator(O.LIST_OF_METRO, station)
        self.wait.until(EC.visibility_of_element_located(locator))
        self.click(locator)

    @allure.step("Внести телефон")
    def set_phone(self,phone_number):
        self.type_text(O.PHONE_NUMBER,phone_number)

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self,name,surname,address,station,phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro()
        self.select_metro(station)
        self.set_phone(phone_number)

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.click(O.NEXT_BUTTON)

    @allure.step("Внести дату заказа")
    def choise_rental_date(self,date):
        self.wait_visible(O.DATE_RENT).send_keys(date, Keys.ENTER)

    @allure.step("Открыть выпадающий список выбора колличества дней аренды")
    def click_rental_period(self):
        self.click(O.RENTAL_PERIOD)

    @allure.step("Выбрать колличество дней арнеды")
    def choice_rental_period(self,lease):
        self.click(self.get_locator(O.RENT_OPTION, lease))

    @allure.step("Выбрать цвет самоката")
    def choice_colour(self,colour):
        self.click(self.get_locator(O.COLOR_SELECT,colour))

    @allure.step("Оставить комментарий")
    def set_comment(self,comment):
        self.type_text(O.COMMENT,comment)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self,date,lease,colour,comment):
        self.choise_rental_date(date)
        self.click_rental_period()
        self.choice_rental_period(lease)
        self.choice_colour(colour)
        self.set_comment(comment)

    @allure.step("Нажать на кнопку Заказать")
    def click_order_button(self):
        self.click(O.ORDER_BUTTON)

    @allure.step("Нажать на кнопку Да")
    def click_yes_button(self):
        self.click(O.YES_BUTTON)

    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        return self.wait_visible(O.ORDER_SUCCESS_MESSAGE)

    @allure.step("Нажать на кнопку Посмотреть статус заказа")
    def click_show_status_button(self):
        self.click(O.SHOW_STATUS_BUTTON)

    @allure.step("Нажать на Логотип Самоката")
    def click_on_scooter_logo(self):
        self.click(O.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекс и перейти на Дзен")
    def click_on_yandex_logo(self):
        self.click(O.YANDEX_LOGO)
        self.switch_to_new_window()
        self.wait_url_contains("dzen")


    