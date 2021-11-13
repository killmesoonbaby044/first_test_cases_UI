from .base_page import BasePage
from .locators import PageLoc

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_to_cart(self):
        self.fe(*PageLoc.add_cart_button).click()
        print('clicked')
        self.solve_quiz_and_get_code()

    def should_be_guest_see_success_message_after_adding_product_to_basket(self):
        self.open()
        self.fe(*PageLoc.add_cart_button).click()
        print('added to cart\n')
        assert not self.is_not_element_present(*PageLoc.name_book_loc), \
            "Success message is presented, but should not be"

    def should_be_guest_cant_see_success_message(self):
        self.open()
        assert self.is_not_element_present(*PageLoc.name_book_loc), \
            "Success message is presented, but should not be"

    def should_be_message_disappeared_after_adding_product_to_basket(self):
        self.open()
        self.fe(*PageLoc.add_cart_button).click()
        print('checking disappearing')
        assert self.is_disappeared(*PageLoc.name_book_loc), \
            "Success message is presented, but should be disappeared"

    def should_be_added_item_name(self):
        wait = WebDriverWait(self.browser, 10)
        name_book = wait.until(EC.visibility_of_element_located(PageLoc.name_book_loc)).text
        true_name = self.fe(*PageLoc.true_name_book_loc).text
        print('Checking names')
        assert name_book == true_name, "WRONG NAME OF BOOK!"

    def should_be_added_item_price(self):
        price = self.fe(*PageLoc.true_price_loc).text.split(' ')[0]
        site_price = self.fe(*PageLoc.price_loc).text.split(' ')[0]
        print('Checking prices')
        assert price == site_price, "WRONG PRICE!"

    def guest_can_go_to_login_page_from_product_page(self):
        self.go_to_login_page()
        self.should_be_login_page()
