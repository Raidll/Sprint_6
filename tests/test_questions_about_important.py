import allure
import pytest

from data.urls import URLS
from page_objects.home_page import HomePage
from data.home_page_constants import HomePageConstants


class TestQuestionsAboutImportant:
    @allure.title('Проверка ответов на вопросы раздела Вопросы о важном')
    @allure.description('Проверка наличия необходимых вопросов и соответствия им корректных ответов из разделе '
                        'Вопросы о важном')
    @pytest.mark.parametrize('question_xpath,answer_xpath,question_text,answer_text', HomePageConstants.questions_and_answers)
    def test_checking_questions_and_answers(self, driver, question_xpath, answer_xpath, question_text, answer_text):
        driver.get(URLS.HOME_PAGE)

        home_page = HomePage(driver)
        home_page.scroll_to_element_by_xpath(question_xpath)
        home_page.waiting_visibility_by_xpath(question_xpath)
        home_page.click_by_xpath(question_xpath)
        home_page.waiting_visibility_by_xpath(answer_xpath)
        assert (driver.find_element(*question_xpath).text == question_text) and (driver.find_element(*answer_xpath).text == answer_text)

