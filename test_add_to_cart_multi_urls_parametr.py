from .pages_add_to_cart.product_page import ProductPage
import pytest

# TESTING ONLY NAME OF BOOK WITHOUT PRICE on few pages
urls = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" \
        f"?promo=offer{numb}" for numb in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_added_item_name()
