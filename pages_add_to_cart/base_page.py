from .locators import BPLoc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

import math


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        print(f"\nopen link {self.url}")
        self.browser.get(self.url)

    def fe(self, how, what):
        return self.browser.find_element(how, what)

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 4). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 4). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, 4, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.browser.find_element(*BPLoc.LOGIN_LINK).click()

    def should_be_login_page(self):
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', \
            'INCORRECT PAGE (NOT A LOGIN PAGE)'

    def should_be_login_link(self):
        assert self.is_element_present(*BPLoc.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        self.fe(*BPLoc.basket_button_loc).click()





    def solve_quiz_and_get_code(self):
        print('start quizMATHcode')
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
