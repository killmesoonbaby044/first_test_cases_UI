from .pages_add_to_cart.product_page import ProductPage

# TEST FOR RIGHT NAME AND PRICE ON 1 PAGE


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    print('added')
    page.should_be_added_item_name()
    print('name')
    page.should_be_added_item_price()


