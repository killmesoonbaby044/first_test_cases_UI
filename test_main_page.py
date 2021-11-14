from .pages_add_to_cart.basket_page import BasketPage
import pytest


@pytest.mark.basket
class TestBasket:
    link = 'http://selenium1py.pythonanywhere.com'

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, self.link)
        page.open()
        page.should_be_empty_basket()




