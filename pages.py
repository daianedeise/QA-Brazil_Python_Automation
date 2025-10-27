from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Campos de origem e destino
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Selecionar tarifa e chamar taxi
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"Chamar")]')
    confort_icon_locator = (By.XPATH, '//img[contains(@src,"kids")]')
    confort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    # Número de telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # Método de pagamento
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    # Adicionar comentário
    add_comment = (By.ID, 'comment')

    # Pedir lençóis e cobertor
    switch_blanket = (By.CSS_SELECTOR, '.switch')
    switch_blanket_active = (By.CSS_SELECTOR, '#root .reqs-body .r-sw input')

    # Pedir sorvete
    add_icecream = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')

    # Chamar taxi
    call_taxi_button = (By.CSS_SELECTOR, '.order-header-title')
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    #  ROTAS

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    #  TARIFA

    def click_taxi_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.taxi_option_locator)
        ).click()

    def click_comfort_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confort_icon_locator)
        ).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.confort_active)
            )
            return "active" in active_button.get_attribute("class")
        except:
            return False

    # TELEFONE

    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()
        self.driver.find_element(*self.number_enter).send_keys(telefone)
        self.driver.find_element(*self.number_confirm).click()

        code = retrieve_phone_code(self.driver)
        code_input = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.number_code)
        )
        code_input.clear()
        code_input.send_keys(code)
        self.driver.find_element(*self.code_confirm).click()

    def numero_confirmado(self):
        numero = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.number_finish)
        )
        return numero.text

    # CARTÃO

    def click_add_cartao(self, cartao, code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        time.sleep(1)
        self.driver.find_element(*self.number_card).send_keys(cartao)
        time.sleep(1)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(1)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.close_button_card).click()

    def confirm_cartao(self):
        return self.driver.find_element(*self.confirm_card).text

    # COMENTÁRIO

    def add_comentario(self, comentario):
        self.driver.find_element(*self.add_comment).send_keys(comentario)

    def coment_confirm(self):
        return self.driver.find_element(*self.add_comment).get_attribute('value')

    #COBERTOR

    def switch_cobertor(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.switch_blanket)
        ).click()

    def switch_cobertor_active(self):
        switch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.switch_blanket_active)
        )
        return switch.is_selected()

    #SORVETE

    def add_ice(self):
        self.driver.find_element(*self.add_icecream).click()

    def qnt_sorvete(self):
        return self.driver.find_element(*self.qnt_icecream).text

    # CHAMAR TAXI

    def call_taxi(self):
        self.call_taxi_button = (By.ID, "call-taxi")

    def pop_up_show(self):
        try:
            pop_up = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.pop_up)
            )
            return pop_up.text
        except:
            return ""
