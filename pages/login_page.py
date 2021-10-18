from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
 def should_be_login_page(self):
  self.should_be_login_url()
  self.should_be_login_form()
  self.should_be_register_form()

 def should_be_login_url(self):
  assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"
  login_link=self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
  login_link.click()
  URL_STRING=self.browser.current_url
  assert (URL_STRING.find('login')>-1), "The url not contains login-word"
        
 def should_be_login_form(self):
  assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

 def should_be_register_form(self):
  assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

 def register_new_user(self, email, password):
  email = str(time.time()) + "@fakemail.org"
  password=str(time.time()) +"asd!"
  self.enter_data(*LoginPageLocators.REGISTRATION_EMAIL,email)
  self.enter_data(*LoginPageLocators.REGISTRATION_PASS,password)
  self.enter_data(*LoginPageLocators.REGISTRATION_PASS_AGAIN,password)
  button=self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
  button.click()