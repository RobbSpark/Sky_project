import time
import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

@pytest.mark.now
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Hyg7^gcfr%hd"
        self.page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        self.page.open()
        self.page.register_new_user(email, password)
        self.final_page = MainPage(browser, browser.current_url)
        self.final_page.should_be_authorized_user()
        yield
        self.acc_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/profile/')
        self.acc_page.open()
        self.acc_page.delete_user_profile(password)


    LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_user_can_add_product_to_basket(self, browser):
        self.page = ProductPage(browser, self.LINK)
        self.page.open()
        self.page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        self.page = ProductPage(browser, self.LINK)
        self.page.open()
        self.page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('link2', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="some bug")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link2):
    link = f"{link2}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

@pytest.mark.xfail
def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()


@pytest.mark.smoke
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.smoke
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.basket_should_not_have_products()
    basket_page.should_be_message_basket_is_empty()


