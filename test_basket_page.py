from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


def test_guest_can_see_product_in_basket_after_adding_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_basket_is_empty()
    basket_page.basket_should_not_have_products()
