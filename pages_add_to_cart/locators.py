from selenium.webdriver.common.by import By


class PPLoc:
    add_cart_button = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    name_book_loc = (By.CSS_SELECTOR, '#messages strong')
    true_name_book_loc = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    true_price_loc = (By.CSS_SELECTOR, '.col-sm-6>.price_color')
    price_loc = (By.CSS_SELECTOR, '.alertinner p strong')
    rofl = (By.CSS_SELECTOR, 'asdads')


class BPLoc:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket_button_loc = (By.CSS_SELECTOR, '.btn-group>a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPLoc:
    empty_basket_loc = (By.CSS_SELECTOR, '#content_inner>p>a')
    basket_element_loc = (By.CLASS_NAME, 'basket-items')


class LoginPLoc:
    email = (By.ID, 'id_registration-email')
    pass1 = (By.ID, 'id_registration-password1')
    pass2 = (By.ID, 'id_registration-password2')
    reg_but = (By.NAME, 'registration_submit')
