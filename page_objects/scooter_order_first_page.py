import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ScooterOrderFirstPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    INPUT_NAME = By.XPATH, ".//input[@placeholder='* Имя']"
    INPUT_SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    INPUT_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    SELECT_METRO_STATION = By.XPATH, ".//input[@class='select-search__input']"
    INPUT_TELEPHONE_NUMBER = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    CHERKIZOVSKAYA_STATION = By.XPATH, ".//div[text()='Черкизовская']"
    BUTTON_NEXT = By.XPATH, ".//button[text()='Далее']"

    @allure.step('Заполнить поле Имя')
    def fill_name(self, name):
        self.fill_field_by_xpath(self.INPUT_NAME, name)

    @allure.step('Заполнить поле Фамилия')
    def fill_surname(self, surname):
        self.fill_field_by_xpath(self.INPUT_SURNAME, surname)

    @allure.step('Заполнить поле Адресс')
    def fill_address(self, address):
        self.fill_field_by_xpath(self.INPUT_ADDRESS, address)

    @allure.step('Заполнить поле Номер телефона')
    def fill_telephone_number(self, number):
        self.fill_field_by_xpath(self.INPUT_TELEPHONE_NUMBER, number)

    @allure.step('Нажать на выбор станции метро')
    def click_select_metro_station(self):
        self.click_by_xpath(self.SELECT_METRO_STATION)

    @allure.step('Выбрать станция Черкизовская из списка')
    def click_cherkizovskaya_station(self):
        self.click_by_xpath(self.CHERKIZOVSKAYA_STATION)

    @allure.step('Клик по кнопке Далее')
    def click_button_next(self):
        self.click_by_xpath(self.BUTTON_NEXT)


