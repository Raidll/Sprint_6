import allure
from selenium.webdriver.common.by import By


class ScooterOrderFirstPage:
    def __init__(self, driver):
        self.driver = driver

    INPUT_NAME = By.XPATH, ".//input[@placeholder='* Имя']"
    INPUT_SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    INPUT_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    SELECT_METRO_STATION = By.XPATH, ".//input[@class='select-search__input']"
    INPUT_TELEPHONE_NUMBER = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    CHERKIZOVSKAYA_STATION = By.XPATH, ".//div[text()='Черкизовская']"
    BUTTON_NEXT = By.XPATH, ".//button[text()='Далее']"

    @allure.step('Заполнить поле Имя')
    def fill_name(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)

    @allure.step('Заполнить поле Фамилия')
    def fill_surname(self, surname):
        self.driver.find_element(*self.INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполнить поле Адресс')
    def fill_address(self, address):
        self.driver.find_element(*self.INPUT_ADDRESS).send_keys(address)

    @allure.step('Заполнить поле Номер телефона')
    def fill_telephone_number(self, number):
        self.driver.find_element(*self.INPUT_TELEPHONE_NUMBER).send_keys(number)

    @allure.step('Нажать на выбор станции метро')
    def click_select_metro_station(self):
        self.driver.find_element(*self.SELECT_METRO_STATION).click()

    @allure.step('Выбрать станция Черкизовская из списка')
    def click_cherkizovskaya_station(self):
        self.driver.find_element(*self.CHERKIZOVSKAYA_STATION).click()

    @allure.step('Клик по кнопке Далее')
    def click_button_next(self):
        self.driver.find_element(*self.BUTTON_NEXT).click()


