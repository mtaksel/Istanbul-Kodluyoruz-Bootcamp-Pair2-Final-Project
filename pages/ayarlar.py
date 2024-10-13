from time import sleep
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.ayarlar_constants import *
from pages.constants.giris_constants import *


@pytest.mark.usefixtures("setup")
class Ayarlar(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def ana_giris(self):
        user_name= self.wait_element_visibility(USERNAME_LOCATOR)
        user_name.send_keys(GIRIS_MAIL)
        password = self.wait_element_visibility(PASSWORD_LOCATOR)
        password.send_keys(MEVCUT_SIFRE)
        self.wait_element_clickable(GIRISYAPBUTTON_LOCATOR).click()
        sleep(2)
        

    def sayfayi_asagi_indir(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")    

    def profil_olustur_bul_tikla(self):
        sleep(2)
        profil_oluştur = self.wait_element_visibility(PROFIL_OLUSTUR_LOCATOR)
        profil_oluştur.click()

    def ayarlar_butonuna_tikla(self):
        ayarlar_butonu = self.wait_element_visibility(AYARLAR_BUTONU_LOCATOR)
        ayarlar_butonu.click()

    def eski_sifre_bul_ve_gönder(self, data):
        eski_sifre = self.wait_element_visibility(ESKI_SIFRE_LOCATOR)
        eski_sifre.send_keys(data)

    def yeni_sifre_bul_ve_gönder(self, data):
        yeni_sifre = self.wait_element_visibility(YENI_SIFRE_LOCATOR)
        yeni_sifre.send_keys(data)

    def yeni_sifre_tekrar_bul_ve_gönder(self, data):
        yeni_sifre_tekrar = self.wait_element_visibility(YENI_SIFRE_TEKRAR_LOCATOR)
        yeni_sifre_tekrar.send_keys(data)

    def error_line_bul_döndür(self):
        error_line = self.wait_element_presence(ERROR_LINE_LOCATOR)
        return error_line.text

    def toast_mesaji_bul_text_döndür(self):
        toast_message = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
        return toast_message.text

    def alert_mesaji_bul_döndür(self):
        alert_message = self.wait_element_presence(ALERT_MESSAGE_LOCATOR)
        return alert_message.text

    def hayir_butonu_bul_döndür(self):
        hayır_butonu = self.wait_element_visibility(HAYIR_BUTONU_LOCATOR)
        return hayır_butonu.text
    
    def evet_butonu_bul_döndür(self):
        evet_butonu = self.wait_element_visibility(EVET_BUTONU_LOCATOR)
        return evet_butonu.text

    def sifremi_degistir_butonunu_bul_tikla(self):
        self.wait_element_clickable(SIFRE_DEGISTIR_BUTONU_LOCATOR).click()

    def üyeligi_sonlandir_butonunu_bul_tikla(self):
        self.wait_element_clickable(UYELIGI_SONLANDIR_LOCATOR).click()

    