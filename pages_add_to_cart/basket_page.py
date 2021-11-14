from .locators import BasketPLoc
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.go_to_basket()
        assert self.is_not_element_present(*BasketPLoc.basket_element_loc)
        assert self.is_element_present(*BasketPLoc.empty_basket_loc)
