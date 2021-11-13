from .pages_add_to_cart.basket_page import BasketPage
import pytest

urls = ['http://selenium1py.pythonanywhere.com',
        'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/' ]


@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = BasketPage(browser, link)
    page.open()
    page.should_be_empty_basket()




