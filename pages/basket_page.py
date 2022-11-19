
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "It isn't basket page"

    def basket_should_not_have_products(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEM) == False, "Basket is not empty"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), "Message 'empty basket' is not presented"
