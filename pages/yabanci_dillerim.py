import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.yabanciDillerimConstants import *
from pages.giris import Giris
from selenium.webdriver import ActionChains, Keys 


@pytest.mark.usefixtures("setup")
class Yabanci_dil_ekle(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    def profilim_kismina_tikla(self):
        time.sleep(5)
        self.wait_element_visibility(PROFILIMBUTTON).click()
    
    def profil_bilgileri_tikla(self):
        self.wait_element_visibility(PROFILBILGILERIMBUTTON).click()
        time.sleep(5)
    
    def yabanci_dillerim_tikla(self):
        self.wait_element_visibility(YABANCIDILLERIM_BUTTON).click()
        time.sleep(5)

    def dil_acilirmenu_tikla(self):
        self.wait_element_visibility(YABANCIDIL_ACILIRMENU).click()
        time.sleep(3)

    def yabancidil_sec(self):
        self.wait_element_visibility(ALMANCASEC).click()
        time.sleep(3)
    
    def seviye_acilirmenu_tikla(self):
        self.wait_element_visibility(SEVIYESEC_ACILIRMENU).click()
        time.sleep(3)
    
    def seviye_sec(self):
        self.wait_element_visibility(SEVIYESEC).click()

    time.sleep(6)
    def kaydet(self):
        self.wait_element_visibility(KAYDET_BUTTON).click()
        
    def kaydetme_basarili(self):
        actual_result_message = self.wait_element_presence(SAVE_LANGUAGE_POPUP_XPATH)
        return actual_result_message.text


class Yabanci_dil_bos_gecme(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def profilim_kismina_tikla(self):
        time.sleep(5)
        self.wait_element_visibility(PROFILIMBUTTON).click()
    
    def profil_bilgileri_tikla(self):
        self.wait_element_visibility(PROFILBILGILERIMBUTTON).click()
        time.sleep(5)
    
    def yabanci_dillerim_tikla(self):
        self.wait_element_visibility(YABANCIDILLERIM_BUTTON).click()
        time.sleep(5)

    def dil_acilirmenu_tikla(self):
        self.wait_element_visibility(YABANCIDIL_ACILIRMENU).click()
        time.sleep(3)

    def yabancidil_sec(self):
        self.wait_element_visibility(ALMANCASEC).click()
        time.sleep(3)
    
    def seviye_acilirmenu_tikla(self):
        self.wait_element_visibility(SEVIYESEC_ACILIRMENU).click()
        time.sleep(3)

    def kaydet(self):
        self.wait_element_visibility(KAYDET_BUTTON).click()
        time.sleep(3)

    def doldurulmasi_zorunlu_alan_mesaji(self):
        actual_result_message = self.wait_element_presence(BLANK_MESSAGE)
        return actual_result_message.text

class Yabanci_dil_silme(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def profilim_kismina_tikla(self):
        time.sleep(5)
        self.wait_element_visibility(PROFILIMBUTTON).click()
    
    def profil_bilgileri_tikla(self):
        self.wait_element_visibility(PROFILBILGILERIMBUTTON).click()
    time.sleep(5)
    
    def yabanci_dillerim_tikla(self):
        self.wait_element_visibility(YABANCIDILLERIM_BUTTON).click()
    time.sleep(5)

    def sil_butonuna_tikla(self):
        aChains = ActionChains(self.driver)
        hover_on = self.wait_element_visibility(HOVER_ON_LAGNGUAGE)
        aChains.move_to_element(hover_on).perform()
        time.sleep(7)
        self.wait_element_visibility((DELETE_BUTTON_XPATH)).click()
    time.sleep(5)

    def silmeyi_onayla(self):
        self.wait_element_visibility(CONFIRM_DELETE_XPATH).click()
    
    def silme_islemi_basarili(self):
        silme_popup = self.wait_element_presence( DELETE_POPUP_XPATH)
        return silme_popup.text
    
    
    
    

    
        

 
        