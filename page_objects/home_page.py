import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    TOP_ORDER_BUTTON = By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']"

    BOTTOM_ORDER_BUTTON = By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']"

    XPATH_FIRST_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-0']"
    XPATH_SECOND_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-1']"
    XPATH_THIRD_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-2']"
    XPATH_FOURTH_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-3']"
    XPATH_FIFTH_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-4']"
    XPATH_SIXTH_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-5']"
    XPATH_SEVENTH_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-6']"
    XPATH_EIGHTH_QUESTION_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__heading-7']"

    XPATH_FIRST_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-0']"
    XPATH_SECOND_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-1']"
    XPATH_THIRD_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-2']"
    XPATH_FOURTH_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-3']"
    XPATH_FIFTH_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-4']"
    XPATH_SIXTH_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-5']"
    XPATH_SEVENTH_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-6']"
    XPATH_EIGHTH_ANSWER_ABOUT_IMPORTANT = By.XPATH, ".//div[@id='accordion__panel-7']"

    @allure.step('Клик по верхней кнопке Заказать')
    def click_top_order_button(self):
        self.click_by_xpath(self.TOP_ORDER_BUTTON)

    @allure.step('Клик по нижней кнопке Заказать')
    def click_bottom_order_button(self):
        self.click_by_xpath(self.BOTTOM_ORDER_BUTTON)

    @allure.step('Скролл к нижней кнопке Заказать')
    def scroll_to_bottom_order_button(self):
        self.scroll_to_element_by_xpath(self.BOTTOM_ORDER_BUTTON)
