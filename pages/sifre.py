import re
from time import sleep
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.sifre_constans import *
import pyautogui


@pytest.mark.usefixtures("setup")
class Password(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sifremi_unuttum_butonuna_tikla(self):
        sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
        sifre_unuttum_button.click()

    def mail_input_gönder(self, data):
        mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
        sleep(3)
        self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys(data)
        #mail_input_area.send_keys(data)

    def gönder_butonuna_tikla(self):
        gonder_button = self.wait_element_clickable(GONDER_BUTTON_LOCATOR)
        gonder_button.click()

    def toast_mesaji_bul_ve_içeriği_text_getir(self):
        toast_message_sifre_sifirlama = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
        return toast_message_sifre_sifirlama.text
    
    def gmail_git(self):
        self.driver.get(GMAIL_INBOX_URL)
    
    def gmail_mail_bul_ve_gönder(self):
        gmail_mail= self.wait_element_presence(GMAIL_MAIL_INPUT_LOCATOR).send_keys(SIFIRLAMA_MAIL)
        #self.wait_element_presence(GMAIL_MAIL_INPUT_LOCATOR).send_keys(SIFIRLAMA_MAIL)

    def sonraki_butonuna_tikla(self):
        sleep(3)
        sonraki_butonu = pyautogui.click(1394, 690)
        sleep(5)
        # sonraki_butonu = self.wait_element_visibility(SONRAKI_BUTTON_LOCATOR)
        # sonraki_butonu.click

    def gmail_sifre_bul_ve_gönder(self):
        gmail_sifre = self.wait_element_presence(GMAIL_PASSWORD_INPUT_LOCATOR).send_keys(SIFIRLAMA_TOBETO_SIFRE)

    def gmail_mail_tikla(self):
        gmail_mail = pyautogui.click(570, 310)
        sleep(3)
        # gmail_mail = self.wait_element_presence(GMAIL_MAIL_BUL_LOCATOR).click

    def gmail_sifirlama_linki_tikla(self):
        sifirlama_link = pyautogui.click(1070, 430)
        sleep(3)
        # sifirlama_link = self.wait_element_presence(GMAIL_SIFIRLAMA_LINK_LOCATOR).click

    def yeni_sifre_gönder(self):
        self.wait_element_visibility(SIFRE_SIFIRLAMA_INPUT_LOCATOR).send_keys(SIFIRLAMA_TOBETO_SIFRE)

    def yeni_sifre_kabul_gönder(self):
        self.wait_element_visibility(SIFRE_SIFIRLAMA_INPUT2_LOCATOR).send_keys(SIFIRLAMA_TOBETO_SIFRE) 

    # def sifre_sifirlama(self):
    #     sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
    #     sifre_unuttum_button.click()
    #     mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
    #     self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys(GIRISMAIL)
    #     #mail_input_area.send_keys(GIRISMAIL)
    #     gonder_button = self.wait_element_visibility(GONDER_BUTTON_LOCATOR)
    #     gonder_button.click()
    #     toast_message_sifre_sifirlama = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
    #     return toast_message_sifre_sifirlama.text

    # def sifre_sifirlama_gecersiz_mail(self):
    #     sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
    #     sifre_unuttum_button.click()
    #     mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
    #     self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys("email")
    #     #mail_input_area.send_keys("email")
    #     gonder_button = self.wait_element_visibility(GONDER_BUTTON_LOCATOR)
    #     gonder_button.click()
    #     toast_message_sifre_sifirlama_gecersiz_mail = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
    #     return toast_message_sifre_sifirlama_gecersiz_mail.text
    
    # def sifre_sifirlama_gecersiz_kullanici(self):
    #     sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
    #     sifre_unuttum_button.click()
    #     mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
    #     self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys("tobeto1@gmail.com")
    #     #mail_input_area.send_keys("tobeto1@gmail.com")
    #     gonder_button = self.wait_element_clickable(GONDER_BUTTON_LOCATOR)
    #     gonder_button.click()
    #     toast_message_sifre_sifirlama_gecersiz_kullanici = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
    #     return toast_message_sifre_sifirlama_gecersiz_kullanici.text 
    

    