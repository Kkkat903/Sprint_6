import pytest
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators as M


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,15)

    @allure.step("Дождаться видимости {locator}")
    def wait_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проскролить до конца")
    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
   
    @allure.step("Кликнуть по элементу {locator}")
    def click(self,locator):
        self.wait_clickable(locator).click()

    @allure.step("Дождаться видимости {locator} и нажать на него")
    def click_element_with_wait(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        self.driver.execute_script("arguments[0].click();",element)

    @allure.step("Подставить значение в локатор")
    def get_locator(self,locator,value):
        return (locator[0],locator[1].format(value))

    @allure.step("Внести текст в элемент")
    def type_text(self, locator, text):
        self.wait_visible(locator).send_keys(text)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Проверка содержания {text} в url")
    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Получение адреса страницы")
    def get_current_url(self):
        return self.driver.current_url
