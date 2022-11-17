from allure_commons.types import AttachmentType
from behave import *
import pytest
from conftest import browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import ProductLocators
import allure

from pages.product_page import ProductPage

@allure.severity(allure.severity_level.NORMAL)
@given('I open product page "{link}"')
def open_product_page(context, link):
    context.browser = webdriver.Chrome()
    context.browser.get(link)

@allure.severity(allure.severity_level.NORMAL)
@when("I add the product to the basket")
def add_product_to_basket(context):
    context.browser.find_element(*ProductLocators.ADD_BUTTON).click()

@allure.severity(allure.severity_level.NORMAL)
@then("I see success message")
def step_impl(context):
    allure.attach(context.browser.get_screenshot_as_png(), name="TestSuccessMessageScreenshot", attachment_type=AttachmentType.PNG)
    assert context.browser.find_element(*ProductLocators.SUCCESS_MESSAGE), "Test Passed"
    context.browser.close()


@then("I see message of product added")
def step_impl(context):
    pass


@then("I see that basket total matches product price")
def step_impl(context):
    pass