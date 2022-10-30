from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_button()
        self.press_add_button()
        BasePage.solve_quiz_and_get_code(self)
        self.should_be_message_of_successful_add_to_basket()
        self.should_be_message_of_basket_total()


    def should_be_add_button(self):
        assert self.browser.find_element(*ProductLocators.ADD_BUTTON), "Add button isn't found"

    def press_add_button(self):
        self.browser.find_element(*ProductLocators.ADD_BUTTON).click()

    def should_be_message_of_successful_add_to_basket(self):
        assert self.browser.find_element(*ProductLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductLocators.MES_PRODUCT_ADDED).text, "Product name does not match the added product"

    def should_be_message_of_basket_total(self):
        assert self.browser.find_element(*ProductLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductLocators.MES_BASKET_TOTAL).text, "Product name does not match the added product"
