import data
import helpers
from selenium import webdriver
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.urban_routes_url):
            cls.driver.get(data.urban_routes_url)
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass
    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass
    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill_phone_number")
        pass
    def test_fill_card(self):
        # Add in S8
        print("function created for fill_card")
        pass
    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment_for_driver")
        pass
    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order_blanket_and_handkerchiefs")
        pass
    def test_order_2_ice_creams(self):
        for i in range(2):
            # Add in S8
            pass
        print("function created for order_2_ice_creams")
        pass
    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car_search_model_appears")
        pass
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()