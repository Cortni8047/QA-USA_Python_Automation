import time

from selenium.webdriver import Keys

import helpers
from helpers import  retrieve_phone_code

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class UrbanRoutesPage:


    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    call_taxi_button = (By.XPATH, "//button[text()='Call a taxi']")
    supportive_tariff_button = (By.XPATH, "//div[@class='tcard']")
    supportive_tariff_selected = (By.XPATH, "//div[@class='tcard active']")
    order_button = (By.CLASS_NAME, "smart-button-wrapper")

    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.ID, "phone")
    next_button = (By.XPATH, "//button[contains(text(), 'Next')]")
    confirmation_code_field = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    retrieve_phone_code_field = (By.ID, "code")
    car_search_modal = (By.CLASS_NAME, "order-body")
    phone_code = (By.ID, "code")

    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.CLASS_NAME, "pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.CSS_SELECTOR, "#code.card-input")
    link_button = (By.XPATH, "//button[contains(text(), 'Link')]")
    payment_method_text = (By.CLASS_NAME, "pp-value-text")
    close_payment_modal = (By.XPATH, "//button[@class='close-button section-close']")

    comment_field = (By.ID, "comment")
    checkbox_field = (By.ID, "checked")

    blanket_and_tissues_switch = (By.CLASS_NAME, "switch")
    blanket_and_tissues_checkbox = (By.CLASS_NAME, "switch-input")

    ice_cream_counter_plus = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter_value = (By.CLASS_NAME, "counter-value")
    ice_cream_plus_button = (By.XPATH, "//div[@class='counter-plus']")


    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        time.sleep(2)
        self.driver.find_element(*self.call_taxi_button).click()

    def click_supportive_tariff(self):
        self.driver.find_element(*self.supportive_tariff_button).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def is_supportive_tariff_selected(self):
        try:
            self.driver.find_element(*self.supportive_tariff_selected)
            return True
        except:
            return False

    def set_full_phone(self, number):
        self.click_phone_number_button()
        self.set_phone_number(number)
        self.click_next_button()
        self.set_confirmation_code()
        self.click_confirm_button()

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()


    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_confirmation_code(self):
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.confirmation_code_field).send_keys(code)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).text

    def retrieve_phone_code(self):
        return retrieve_phone_code(self.driver)

    def is_car_search_modal_displayed(self):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.car_search_modal))
        return self.driver.find_element(*self.car_search_modal).is_displayed()

    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)


    def click_link_button(self):
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.link_button).click()

    def close_payment_method_modal(self):
        self.driver.find_element(*self.close_payment_modal).click()

    def get_payment_method_text(self):
        return self.driver.find_element(*self.payment_method_text).text

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.comment_field).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.comment_field).get_attribute("value")

    def click_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_switch).click()

    def get_blanket_checkbox_property(self):
       return self.driver.find_element(*self.blanket_and_tissues_checkbox).get_property('checked')

    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ice_cream_counter_plus).click()

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ice_cream_counter_value).text)

    def click_order_ice_cream(self):
        self.driver.find_element(*self.ice_cream_plus_button).click()

    def order_ice_cream(self, quantity):
        current_count = self.get_ice_cream_count()
        clicks_needed = quantity - current_count
        for _ in range(clicks_needed):
            self.click_ice_cream_plus()