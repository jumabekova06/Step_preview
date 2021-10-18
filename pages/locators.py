from selenium.webdriver.common.by import By


class MainPageLocators():
 LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
 LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
 LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
 REGISTRATION_FORM=(By.CSS_SELECTOR, "#register_form")
 REGISTRATION_EMAIL=(By.CSS_SELECTOR, "#id_registration-email")
 REGISTRATION_PASS=(By.CSS_SELECTOR, "#id_registration-password1")
 REGISTRATION_PASS_AGAIN=(By.CSS_SELECTOR, "#id_registration-password2") 
 REGISTRATION_BUTTON=(By.CSS_SELECTOR, "#register_form > button")
 
class ProductPageLocators():
 ADD_BASKET_BUTTON=(By.CSS_SELECTOR, ".btn-add-to-basket")
 PRODUCT_NAME=(By.CSS_SELECTOR, ".product_main > h1")
 PRODUCT_NAME_ADDING_MESSAGE=(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
 
class BasePageLocators():
 LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
 LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
 BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > span > a")
 USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
 EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")