import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            cls.driver.get(data.URBAN_ROUTES_URL)
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Assert both addresses were set correctly
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()

        assert (routes_page.is_supportive_tariff_selected() == True)


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()
        routes_page.click_phone_number_button()

        routes_page.set_phone_number(data.PHONE_NUMBER)

        phone_code = routes_page.retrieve_phone_code()

        routes_page.click_confirm_button()

        routes_page.set_confirmation_code(phone_code)

        assert routes_page.get_phone_number() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()
        routes_page.click_payment_method_button()
        routes_page.click_add_card_button()
        routes_page.set_card_number(data.CARD_NUMBER)
        routes_page.set_card_code(data.CARD_CODE)
        routes_page.click_link_button()

        assert routes_page.payment_method_text() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()

        routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)

        assert routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()
        routes_page.click_blanket_and_tissues()

        assert routes_page.get_blanket_checkbox_property("checked") == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()

        for i in range(2):
            routes_page.click_order_ice_cream()

        assert routes_page.get_ice_cream_count() == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        routes_page.click_call_taxi_button()
        routes_page.click_supportive_tariff()
        phone_code = routes_page.retrieve_phone_code()

        routes_page.click_phone_number_button()
        routes_page.phone_number_field()
        helpers.retrieve_phone_code()
        routes_page.set_phone_number()
        routes_page.click_confirm_button()
        routes_page.set_confirmation_code(phone_code)
        routes_page.set_message_for_driver()
        routes_page.click_order_button()

        assert routes_page.is_car_search_modal_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()