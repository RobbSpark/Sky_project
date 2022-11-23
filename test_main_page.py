import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

mp_link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        self.page = MainPage(browser, mp_link)
        self.page.open()
        self.page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        self.page = MainPage(browser, mp_link)
        self.page.open()
        self.page.go_to_login_page()

@pytest.mark.now
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, mp_link)
    page.open()
    time.sleep(1)
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_not_have_products()
    basket_page.should_be_message_basket_is_empty()

