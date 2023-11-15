import time

import allure
import pytest

from data.urls import URLS
from page_objects.home_page import HomePage
from data.home_page_constants import HomePageConstants
from page_objects.scooter_order_first_page import ScooterOrderFirstPage
from page_objects.scooter_order_second_page import ScooterOrderSecondPage


class TestOrderAScooter:
    names = ["Иван", "Пётр"]
    surnames = ["Иванов", "Петров"]
    adresses = ["Иванов", "Петрович"]
    telephone_numbers = ["79151111111", "79152222222"]
    dates = ["20.03.2024", "15.01.2025"]
    comments = ["Тестовый комментарий", "Второй тестовый комментарий"]

    @allure.title('Заказ самоката нажатием на верхнюю кнопку Заказать')
    @allure.description('Проверка возможности заказать самокат через меню, открывающееся при нажатии на верхнюю '
                        'кнопку Заказать на главной странице')
    def test_order_a_scooter_top_button(self, driver):
        driver.get(URLS.HOME_PAGE)

        home_page = HomePage(driver)
        home_page.click_top_order_button()

        scooter_order_first_page = ScooterOrderFirstPage(driver)
        scooter_order_first_page.fill_name(self.names[0])
        scooter_order_first_page.fill_surname(self.surnames[0])
        scooter_order_first_page.fill_address(self.adresses[0])
        scooter_order_first_page.click_select_metro_station()
        scooter_order_first_page.click_cherkizovskaya_station()
        scooter_order_first_page.fill_telephone_number(self.telephone_numbers[0])
        scooter_order_first_page.click_button_next()

        scooter_order_second_page = ScooterOrderSecondPage(driver)
        scooter_order_second_page.fill_date(self.dates[0])
        scooter_order_second_page.hide_calendar()
        scooter_order_second_page.click_dropdown_rental_period()
        scooter_order_second_page.click_rental_period_is_one_day()
        scooter_order_second_page.click_checkbox_black()
        scooter_order_second_page.fill_comment(self.comments[0])
        scooter_order_second_page.click_order_button()
        scooter_order_second_page.click_accept_order_button()
        scooter_order_second_page.waiting_visibility_button_check_order_status()

        assert "Посмотреть статус" in driver.find_element(*scooter_order_second_page.CHECK_ORDER_STATUS).text

    @allure.title('Заказ самоката нажатием на нижнюю кнопку Заказать')
    @allure.description('Проверка возможности заказать самокат через меню, открывающееся при нажатии на нижнюю '
                        'кнопку Заказать на главной странице')
    def test_order_a_scooter_buttom_button(self, driver):
        driver.get(URLS.HOME_PAGE)

        home_page = HomePage(driver)

        home_page.scroll_to_bottom_order_button()
        home_page.click_bottom_order_button()

        scooter_order_first_page = ScooterOrderFirstPage(driver)
        scooter_order_first_page.fill_name(self.names[1])
        scooter_order_first_page.fill_surname(self.surnames[1])
        scooter_order_first_page.fill_address(self.adresses[1])
        scooter_order_first_page.click_select_metro_station()
        scooter_order_first_page.click_cherkizovskaya_station()
        scooter_order_first_page.fill_telephone_number(self.telephone_numbers[1])
        scooter_order_first_page.click_button_next()

        scooter_order_second_page = ScooterOrderSecondPage(driver)
        scooter_order_second_page.fill_date(self.dates[1])
        scooter_order_second_page.hide_calendar()
        scooter_order_second_page.click_dropdown_rental_period()
        scooter_order_second_page.click_rental_period_is_one_day()
        scooter_order_second_page.click_checkbox_black()
        scooter_order_second_page.fill_comment(self.comments[1])
        scooter_order_second_page.click_order_button()
        scooter_order_second_page.click_accept_order_button()
        scooter_order_second_page.waiting_visibility_button_check_order_status()

        assert "Посмотреть статус" in driver.find_element(*scooter_order_second_page.CHECK_ORDER_STATUS).text
