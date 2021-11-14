from .base_page import BasePage
from .locators import LoginPLoc


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.fe(*LoginPLoc.email).send_keys(email)
        self.fe(*LoginPLoc.pass1).send_keys(password)
        self.fe(*LoginPLoc.pass2).send_keys(password)
        self.fe(*LoginPLoc.reg_but).click()
    """    
    def should_be_login_pages(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "WE'RE NOT ON LOGIN PAGE"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN), "log is gone"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR), "reg is gone"
    """
