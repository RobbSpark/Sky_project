from .base_page import BasePage
from .locators import LoginPageLocators, ProfilePageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It isn't login url"

    def should_be_login_form(self):
         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form isn't presented"

    def register_new_user(self, email, password):
        print(email, password)
        self.browser.find_element(*LoginPageLocators.REGISTER_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASW).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASW_REPITE).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SEND_BUTTON).click()
        print("user profile was CREATED successfully")

    def delete_user_profile(self, password):
        print("deleting user profile...")
        self.browser.find_element(*ProfilePageLocators.DEL_PROFILE_BTN).click()
        self.browser.find_element(*ProfilePageLocators.DEL_PASW).send_keys(password)
        self.browser.find_element(*ProfilePageLocators.DEL_PROFILE_BTN_FINAL).click()
        if self.is_element_present(*ProfilePageLocators.DEL_MESSAGE_CONFIRM) == True:
            print("user profile was DELETED successfully")
        else:
            print("user profile deleting was FAILED")