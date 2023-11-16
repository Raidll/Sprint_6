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

    @allure.step('Клик по верхней кнопке Заказать')
    def click_top_order_button(self):
        self.click_by_xpath(self.TOP_ORDER_BUTTON)

    @allure.step('Клик по нижней кнопке Заказать')
    def click_bottom_order_button(self):
        self.click_by_xpath(self.BOTTOM_ORDER_BUTTON)

    @allure.step('Скролл к нижней кнопке Заказать')
    def scroll_to_bottom_order_button(self):
        self.scroll_to_element_by_xpath(self.BOTTOM_ORDER_BUTTON)
