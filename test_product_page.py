from .pages_add_to_cart.product_page import ProductPage
from .pages_add_to_cart.basket_page import BasketPage
from .pages_add_to_cart.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


class TestBasket:
    
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.should_be_empty_basket()


class TestLogLink:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.guest_can_go_to_login_page_from_product_page()


class TestGuestAddProd:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_cart()
        page.should_be_added_item_name()
        page.should_be_added_item_price()

    def test_guest_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.should_be_guest_see_success_message_after_adding_product_to_basket()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.should_be_message_disappeared_after_adding_product_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.should_be_guest_cant_see_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        links = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, links)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org",
                               str(time.time()) + "pa33w0rd")
        browser.implicitly_wait(10)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.should_be_guest_see_success_message_after_adding_product_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        print('alert')
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
