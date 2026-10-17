from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as M
import allure

class MainPage(BasePage):

    @allure.step("Разрешить куки")
    def accept_cookie(self):
        self.click_element_with_wait(M.COOKIE_BUTTON)

    @allure.step("Нажать на кнопку Заказать")
    def click_order_button(self, locator):
        self.click_element_with_wait(locator)