import allure
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    YANDEX_LOGO = By.XPATH, ".//img[@alt = 'Yandex']"  # логотип "Яндекс"
    SCOOTER_LOGO = By.XPATH, ".//img[@alt = 'Scooter']"  # логотип "Самокат"

    @allure.step('Клик на логотип яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()

    @allure.step('Клик на логотип Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def get_next_tab(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        next_handle = handles[(handles.index(current_handle) + 1) % len(handles)]
        return next_handle

    def get_current_url(self):
        return self.driver.current_url
