import data
import helpers
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome, DesiredCapabilities
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique o servidor.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO






    def test_select_plan(self):
        # Adicionar em S8
        print("Função criada para definir plan")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Função criada para fill phone number")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para fill card")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para definir order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
            # Adicionar em S8
            print("Função criada para order de sorvete")
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função criada para definir car search model appears")
        pass

        @classmethod
        def teardown_class(cls):
            cls.driver.quit()




