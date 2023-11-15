import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    TOP_ORDER_BUTTON = By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']"

    BOTTOM_ORDER_BUTTON = By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']"

    @allure.step('Ожидание видимости элемента по переданному xpath')
    def waiting_visibility_by_xpath(self, xpath):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(xpath))

    @allure.step('Скролл к элементу, xpath которого передан')
    def scroll_to_element_by_xpath(self, xpath):
        element = self.driver.find_element(*xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу, xpath которого передан')
    def click_by_xpath(self, xpath):
        self.driver.find_element(*xpath).click()

    @allure.step('Клик по верхней кнопке Заказать')
    def click_top_order_button(self):
        self.driver.find_element(*self.TOP_ORDER_BUTTON).click()

    @allure.step('Клик по нижней кнопку Заказать')
    def click_bottom_order_button(self):
        self.driver.find_element(*self.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Скролл к нижней кнопке Заказать')
    def scroll_to_bottom_order_button(self):
        element = self.driver.find_element(*self.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
