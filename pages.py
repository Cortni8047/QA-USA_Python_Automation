from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # FOUNDATIONAL LOCATORS (Steps 1-4)
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    call_taxi_button = (By.CLASS_NAME, "button round")
    supportive_tariff_button = (By.XPATH, "//div[@class='tcard']")
    supportive_tariff_selected = (By.XPATH, "//div[@class='tcard active']")

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def click_supportive_tariff(self):
        self.driver.find_element(*self.supportive_tariff_button).click()

    def is_supportive_tariff_selected(self):
        try:
            self.driver.find_element(*self.supportive_tariff_selected)
            return True
        except:
            return False

    # PHONE NUMBER LOCATORS
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.ID, "phone")
    next_button = (By.CLASS_NAME, "button full")
    confirmation_code_field = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[contains(text(), 'Confirm')]")

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_confirmation_code(self, code):
        self.driver.find_element(*self.confirmation_code_field).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    # PAYMENT METHOD LOCATORS
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.CLASS_NAME, "pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    link_button = (By.XPATH, "//button[contains(text(), 'Link')]")
    payment_method_text = (By.CLASS_NAME, "pp-value-text")
    close_payment_modal = (By.XPATH, "//button[@class='close-button section-close']")

    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def click_link_button(self):
        self.driver.find_element(*self.link_button).click()

    def close_payment_method_modal(self):
        self.driver.find_element(*self.close_payment_modal).click()

    # DRIVER COMMENT LOCATORS
    comment_field = (By.ID, "comment")

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.comment_field).send_keys(message)

    # Blanket and handkerchiefs locators
    blanket_and_tissues_switch = (By.CLASS_NAME, "switch")
    blanket_and_tissues_checkbox = (By.CLASS_NAME, "switch-input")

    # Blanket and handkerchiefs methods
    def click_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_switch).click()

    def is_blanket_and_tissues_selected(self):
        return self.driver.find_element(*self.blanket_and_tissues_checkbox).is_selected()

    # Ice cream locators
    ice_cream_counter_plus = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter_value = (By.CLASS_NAME, "counter-value")

    # Ice cream methods
    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ice_cream_counter_plus).click()

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ice_cream_counter_value).text)

    def order_ice_cream(self, quantity):
        current_count = self.get_ice_cream_count()
        clicks_needed = quantity - current_count
        for _ in range(clicks_needed):
            self.click_ice_cream_plus()