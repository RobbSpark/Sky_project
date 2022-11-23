from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY = (By.XPATH, "//div[@id='content_inner']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_MAIL = (By.ID, "id_registration-email")
    REGISTER_PASW = (By.ID, "id_registration-password1")
    REGISTER_PASW_REPITE = (By.ID, "id_registration-password2")
    REGISTER_SEND_BUTTON = (By.NAME, "registration_submit")

class ProfilePageLocators():
    DEL_PROFILE_BTN = (By.ID, "delete_profile")
    DEL_PASW = (By.ID, "id_password")
    DEL_PROFILE_BTN_FINAL = (By.CSS_SELECTOR, ".btn.btn-lg.btn-danger")
    DEL_MESSAGE_CONFIRM = (By.CSS_SELECTOR, ".alertinner.wicon")

class ProductLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    MES_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    MES_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
