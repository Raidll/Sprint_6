import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    YANDEX_LOGO = By.XPATH, ".//img[@alt = 'Yandex']"  # логотип "Яндекс"
    SCOOTER_LOGO = By.XPATH, ".//img[@alt = 'Scooter']"  # логотип "Самокат"

    @allure.step('Клик на логотип яндекса')
    def click_yandex_logo(self):
        self.click_by_xpath(self.YANDEX_LOGO)

    @allure.step('Клик на логотип Самоката')
    def click_scooter_logo(self):
        self.click_by_xpath(self.SCOOTER_LOGO)

    def get_next_tab(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        next_handle = handles[(handles.index(current_handle) + 1) % len(handles)]
        return next_handle

    def switch_window_to_next_tab(self):
        self.driver.switch_to.window(self.get_next_tab())

    def get_current_url(self):
        return self.driver.current_url

    def waiting_visibility_by_xpath(self, xpath):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(xpath))

    def scroll_to_element_by_xpath(self, xpath):
        element = self.driver.find_element(*xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_by_xpath(self, xpath):
        self.driver.find_element(*xpath).click()

    def fill_field_by_xpath(self, xpath, message):
        self.driver.find_element(*xpath).send_keys(message)



