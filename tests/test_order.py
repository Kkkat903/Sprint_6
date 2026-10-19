from pages.order_page import OrderPage
from pages.main_page import MainPage
import pytest
import allure
from data import ORDER_DATA
from urls import Url as U


class TestOrderScooter:
    @allure.title("Позитивная проверка заказа самоката")
    @allure.description("Позитивный флоу заказа: нажать «Заказать», заполнить обе формы, подтвердить заказ, проверить окно об успешном заказе, вернуться на главную по логотипу Самоката и проверить редирект на Дзен по логотипу Яндекса.")
    
    @pytest.mark.parametrize("order_locator,name,surname,address,station,phone_number,date,lease,colour,comment",ORDER_DATA)

    def test_order_scooter(self,driver,order_locator,name,surname,address,station,phone_number,date,lease,colour,comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookie()
        main_page.click_order_button(order_locator)
        order_page.fill_first_form(name,surname,address,station,phone_number)
        order_page.click_next_button()
        order_page.fill_second_form(date,lease,colour,comment)
        order_page.click_order_button()
        order_page.click_yes_button()

        with allure.step("Проверить окно об успешном оформлении заказа"):
            assert "Заказ оформлен" in order_page.get_success_message().text

    def test_click_on_scooter_logo(self,driver):
        order_page = OrderPage(driver)
        order_page.click_on_scooter_logo()

        with allure.step("Проверить переход на главную страницу Самоката"):
            assert order_page.get_current_url() == U.BASE_URL

    def test_click_on_yandex_logo(self,driver):
        order_page = OrderPage(driver)
        order_page.click_on_yandex_logo()

        with allure.step("Проверить, что открылась главная страница Дзена"):
            assert "dzen" in order_page.get_current_url()