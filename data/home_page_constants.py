from selenium.webdriver.common.by import By

from page_objects.home_page import HomePage


class HomePageConstants:
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

    FIRST_QUESTION_TEXT = 'Сколько это стоит? И как оплатить?'
    FIRST_ANSWER_TEXT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    SECOND_QUESTION_TEXT = 'Хочу сразу несколько самокатов! Так можно?'
    SECOND_ANSWER_TEXT = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')
    THIRD_QUESTION_TEXT = 'Как рассчитывается время аренды?'
    THIRD_ANSWER_TEXT = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                         'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                         'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    FOURTH_QUESTION_TEXT = 'Можно ли заказать самокат прямо на сегодня?'
    FOURTH_ANSWER_TEXT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    FIFTH_QUESTION_TEXT = 'Можно ли продлить заказ или вернуть самокат раньше?'
    FIFTH_ANSWER_TEXT = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                         'номеру 1010.')
    SIXTH_QUESTION_TEXT = 'Вы привозите зарядку вместе с самокатом?'
    SIXTH_ANSWER_TEXT = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                         'кататься без передышек и во сне. Зарядка не понадобится.')
    SEVENTH_QUESTION_TEXT = 'Можно ли отменить заказ?'
    SEVENTH_ANSWER_TEXT = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                           'Все же свои.')
    EIGHTH_QUESTION_TEXT = 'Я жизу за МКАДом, привезёте?'
    EIGHTH_ANSWER_TEXT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    questions_and_answers = [
        [XPATH_FIRST_QUESTION_ABOUT_IMPORTANT, XPATH_FIRST_ANSWER_ABOUT_IMPORTANT, FIRST_QUESTION_TEXT, FIRST_ANSWER_TEXT],
        [XPATH_SECOND_QUESTION_ABOUT_IMPORTANT, XPATH_SECOND_ANSWER_ABOUT_IMPORTANT, SECOND_QUESTION_TEXT, SECOND_ANSWER_TEXT],
        [XPATH_THIRD_QUESTION_ABOUT_IMPORTANT, XPATH_THIRD_ANSWER_ABOUT_IMPORTANT, THIRD_QUESTION_TEXT, THIRD_ANSWER_TEXT],
        [XPATH_FOURTH_QUESTION_ABOUT_IMPORTANT, XPATH_FOURTH_ANSWER_ABOUT_IMPORTANT, FOURTH_QUESTION_TEXT, FOURTH_ANSWER_TEXT],
        [XPATH_FIFTH_QUESTION_ABOUT_IMPORTANT, XPATH_FIFTH_ANSWER_ABOUT_IMPORTANT, FIFTH_QUESTION_TEXT, FIFTH_ANSWER_TEXT],
        [XPATH_SIXTH_QUESTION_ABOUT_IMPORTANT, XPATH_SIXTH_ANSWER_ABOUT_IMPORTANT, SIXTH_QUESTION_TEXT, SIXTH_ANSWER_TEXT],
        [XPATH_SEVENTH_QUESTION_ABOUT_IMPORTANT, XPATH_SEVENTH_ANSWER_ABOUT_IMPORTANT, SEVENTH_QUESTION_TEXT, SEVENTH_ANSWER_TEXT],
        [XPATH_EIGHTH_QUESTION_ABOUT_IMPORTANT, XPATH_EIGHTH_ANSWER_ABOUT_IMPORTANT, EIGHTH_QUESTION_TEXT, EIGHTH_ANSWER_TEXT],
    ]
