from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
 def add_button_actions(self):
  assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Basket-button is not presented"
  basket=self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
  basket.click()
  self.solve_quiz_and_get_code()
 
 def names_matched(self):
  assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text==self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDING_MESSAGE).text, \
 "Product name is not matching product name after adding to basket"
 
 def cant_see_success_message_after_adding_product_to_basket(self):
  assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ADDING_MESSAGE), "Success message is presented, but should not be"
 
 def cant_see_success_message(self):
  assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ADDING_MESSAGE), "Success message is presented, but should not be"
  
 def message_disappeared_after_adding_product_to_basket(self):
  assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ADDING_MESSAGE), "Success message is disappeared after adding to basket"