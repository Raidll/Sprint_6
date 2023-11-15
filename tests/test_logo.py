import time

import allure

from page_objects.base_page import BasePage
from data.urls import URLS


class TestLogo:
    @allure.title('Проверка кликабельности логотипа Яндекса')
    @allure.description('При клике на логотип яндекса происходит переход на Дзен')
    def test_click_yandex(self, driver):
        driver.get(URLS.HOME_PAGE)

        base_page = BasePage(driver)
        base_page.click_yandex_logo()
        driver.switch_to.window(base_page.get_next_tab())
        current_url = driver.current_url

        assert URLS.DZEN_URL in current_url

    @allure.title('Проверка редиректа после клика на логотип Самоката')
    @allure.description('При клике на логотип самоката происходит переход на главную страницу')
    def test_click_logo_scooter(self, driver):
        driver.get(URLS.ORDER_PAGE)

        base_page = BasePage(driver)
        base_page.click_scooter_logo()

        current_url = driver.current_url
        assert URLS.HOME_PAGE == current_url
