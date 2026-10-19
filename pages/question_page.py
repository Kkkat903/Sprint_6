import allure
from locators.main_page_locators import MainPageLocators as M
from pages.base_page import BasePage

class QuestionPage(BasePage):

    @allure.step("Нажать на вопрос с подставлением {value}")
    def click_question(self,value):
        locator = self.get_locator(M.QUESTION,value)
        self.scroll_to_element
        self.click_element_with_wait(locator)

    @allure.step("Получить текст ответа с подставлением {value}")
    def get_answer(self,value):
        locator = self.get_locator(M.ANSWER,value)
        return self.wait_visible(locator).text
