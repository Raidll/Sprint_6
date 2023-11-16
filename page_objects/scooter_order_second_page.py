import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class ScooterOrderSecondPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    SCOOTER_DELIVERY_DATE = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    DROPDOWN_RENTAL_PERIOD = By.XPATH, ".//div[text()='* Срок аренды']"
    RENTAL_PERIOD_IS_ONE_DAY = By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='сутки']"
    CHECKBOX_BLACK = By.XPATH, ".//input[@id='black']"
    INPUT_COMMENT = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"
    OUTSIDE = By.XPATH, ".//div[text()='Про аренду']"  # Xpath вне заполняемых полей. Нужен, чтобы скрыть календарь
    ACCEPT_ORDER_BUTTON = By.XPATH, ".//button[text()='Да']"
    CHECK_ORDER_STATUS = By.XPATH, ".//button[text()='Посмотреть статус']"

    @allure.step('Заполнить поле Дата')
    def fill_date(self, date):
        self.fill_field_by_xpath(self.SCOOTER_DELIVERY_DATE, date)

    @allure.step('Клик по полю выбора периода аренды')
    def click_dropdown_rental_period(self):
        self.click_by_xpath(self.DROPDOWN_RENTAL_PERIOD)

    @allure.step('Выбрать период аренды один день')
    def click_rental_period_is_one_day(self):
        self.click_by_xpath(self.RENTAL_PERIOD_IS_ONE_DAY)

    @allure.step('Выбрать чекбокс Черный')
    def click_checkbox_black(self):
        self.click_by_xpath(self.CHECKBOX_BLACK)

    @allure.step('Заполнить поле комментария')
    def fill_comment(self, comment):
        self.fill_field_by_xpath(self.INPUT_COMMENT, comment)

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.click_by_xpath(self.ORDER_BUTTON)

    @allure.step('Клик в стороннее место, чтобы скрыть календарь')
    def hide_calendar(self):
        self.click_by_xpath(self.OUTSIDE)

    @allure.step('Нажать кнопку подтверждения заказа')
    def click_accept_order_button(self):
        self.click_by_xpath(self.ACCEPT_ORDER_BUTTON)

    @allure.step('Ожидание видимости статуса заказа')
    def waiting_visibility_button_check_order_status(self):
        self.waiting_visibility_by_xpath(self.CHECK_ORDER_STATUS)
