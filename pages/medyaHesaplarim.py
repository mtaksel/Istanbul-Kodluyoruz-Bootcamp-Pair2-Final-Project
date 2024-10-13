import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.medyaHesaplarimConstants import *
from pages.giris import Giris
from pages.yabanci_dillerim import *
from selenium.webdriver import ActionChains, Keys 


@pytest.mark.usefixtures("setup")
class Medya_hesabi_ekle(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def medya_hesaplarima_tikla(self):
        self.wait_element_visibility(MEDYA_HESAPLARIM_BUTTON).click()
        time.sleep(3)
    

    def medya_acilir_menu_tikla(self):
        self.wait_element_visibility(MEDYA_ACILIR_MENU).click()
        time.sleep(3)

    def medya_sec(self):
        self.wait_element_visibility(INSTAGRAM_SEC).click()
        time.sleep(3)
    
    def medya_url_gir(self):
        medya_url = self.wait_element_visibility(SEND_URL)
        medya_url.send_keys(URL)
    def medya_kaydet(self):
        self.wait_element_visibility(SAVE_SOCIALMEDIA).click()

    def basarili_kaydetme(self):
        actual_result_popup = self.wait_element_presence(BASARILI_POPUP)
        return actual_result_popup.text
  
    
class Medya_hesabi_bos_alan_kontrolu(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def medya_hesaplarima_tikla(self):
        self.wait_element_visibility(MEDYA_HESAPLARIM_BUTTON).click()
        time.sleep(3)
    

    def medya_acilir_menu_tikla(self):
        self.wait_element_visibility(MEDYA_ACILIR_MENU).click()
        time.sleep(3)

    def medya_sec(self):
        self.wait_element_visibility(INSTAGRAM_SEC).click()
        time.sleep(3)

    def medya_kaydet(self):
        self.wait_element_visibility(SAVE_SOCIALMEDIA).click()

    def bos_alan_kaydetme(self):
        actual_result_message = self.wait_element_visibility(BLANK_AREA_CSS)
        return actual_result_message.text

class Eklenen_medya_hesabi_kontrolu(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def medya_hesaplarima_tikla(self):
        self.wait_element_visibility(MEDYA_HESAPLARIM_BUTTON).click()
        time.sleep(3)
    
    def bilgi_mesaji_goruntule(self):
        info_message = self.wait_element_presence(MEDIA_INFO_MESSAGE_CSS)
        return info_message.text

    


class Medya_hesabi_silme(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver  

    def medya_hesaplarima_tikla(self):
        self.wait_element_visibility(MEDYA_HESAPLARIM_BUTTON).click()
        time.sleep(3)

    def silme_butonuna_tikla(self):
        self.wait_element_visibility(MEDIA_DELETE_BUTTON_XPATH).click()
        time.sleep(3)  
    
    def silme_islemini_onayla(self):
        self.wait_element_visibility(MEDIA_DELETE_CONFIRM_XPATH).click()
        time.sleep(3)

    def silme_islemi_basarili(self):
        silme_popup = self.wait_element_presence(MEDIA_DELETE_POPUP_XPATH)
        return silme_popup.text

class Medya_hesabi_guncelle(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver  

    def medya_hesaplarima_tikla(self):
        self.wait_element_visibility(MEDYA_HESAPLARIM_BUTTON).click()
        time.sleep(3)

    def guncelle_butonuna_tikla(self):
        self.wait_element_visibility(MEDIA_UPDATE_BUTTON_XPATH).click()
        time.sleep(3)

    def acilir_menu_tikla(self):
        self.wait_element_visibility(MEDIA_ACILIR_MENU_XPATH).click()
        time.sleep(3)

    def medya_hesabi_sec(self):
        self.wait_element_visibility(MEDIA_TWITTER_XPATH).click()
        time.sleep(2)
    
    def medya_url_gir(self):
        medya_url = self.wait_element_visibility(MEDIA_SEND_URL_XPATH)
        medya_url.clear()
        time.sleep(2)
        medya_url.send_keys(URL_TWITTER)

    def medya_guncelle(self):
        self.wait_element_visibility(MEDIA_UPDATE_BUTTON).click()
        time.sleep(2)

    def guncelleme_islemini_gerceklestir(self):
        guncelleme_popup = self.wait_element_presence(MEDIA_UPDATE_POPUP)
        return guncelleme_popup.text
        

    
