from .pages_add_to_cart.product_page import ProductPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_go_to_login_page_from_product_page()


def test_guest_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.should_be_guest_see_success_message_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.should_be_message_disappeared_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.should_be_guest_cant_see_success_message()



