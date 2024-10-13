import pytest
import time
from pages.PageBase import PageBase
from pages.giris import Giris
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.constants.kayitOlConstance import *

@pytest.mark.usefixtures("setup")
class KayitOlFonksiyonu(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        time.sleep(10)    

   
    def kayitOl_biliglerini_doldurur(self):
        self.wait_element_visibility(ILKKAYITOL).click()
        self.wait_element_visibility(AD).send_keys(kullanici_ad)
        self.wait_element_visibility(SOYAD).send_keys(kullanici_soyad)
        self.wait_element_visibility(EPOSTA).send_keys(kullanici_eposta)
        self.wait_element_visibility(SIFRE).send_keys(valid_password)
        self.driver.execute_script("scrollBy(0,500)")
        time.sleep(10)
        self.wait_element_visibility(SIFRETEKRAR).send_keys(valid_password)
        self.wait_element_visibility(KAYITOL).click()


    def sozlesmeler_sayfasini_doldurur(self):
        self.wait_element_visibility(ACIKRIZAMETNİ).click()
        self.wait_element_visibility(UYELİKSOZLESMESİ).click()
        self.wait_element_visibility(EPOSTAIZNI).click()
        arama_izni = self.wait_element_visibility(ARAMAIZNI)
        arama_izni.click()
        telno_yaz =self.wait_element_visibility(TELNO)
        telno_yaz.send_keys("9195342036")
        time.sleep(25)
        self.wait_element_visibility(DEVAMETBUTTON).click()
        
    def kaydetme_basarili(self):
        kayit_texi = self.wait_element_presence(GORULECEKTEXT_LOCATE)
        return kayit_texi.text
        
    def bos_kayit(self):
        self.wait_element_visibility(ILKKAYITOL).click()
        self.wait_element_visibility(AD).send_keys(kullanici_ad)
        self.wait_element_visibility(AD).clear()
        time.sleep(2)
        self.wait_element_visibility(SOYAD).send_keys(kullanici_soyad)
        self.wait_element_visibility(SOYAD).clear()
        time.sleep(2)
        self.wait_element_visibility(EPOSTA).send_keys("123")
        self.wait_element_visibility(EPOSTA).clear()
        time.sleep(2)
        self.wait_element_visibility(SIFRE).send_keys(valid_password)
        self.wait_element_visibility(SIFRE).clear()
        time.sleep(2)
        self.driver.execute_script("scrollBy(0,200)")
        time.sleep(2)
        self.wait_element_visibility(SIFRETEKRAR).send_keys(valid_password)
        self.wait_element_visibility(SIFRETEKRAR).clear()
        time.sleep(5)
        
    def zorunlu_alan_karsilastirma(self):   
        zorunlu_alan = self.wait_element_visibility(ZORUNLU1) 
        time.sleep(5)
        zorunlu_alan_listesi = [zorunlu_alan]
        zorunlu_alan_sayisi = int(len(zorunlu_alan_listesi))
        
        return zorunlu_alan_sayisi
        
    
    def kayit_ol_biliglerini_epostasiz_doldurur(self):
        self.wait_element_visibility(ILKKAYITOL).click()
        self.wait_element_visibility(AD).send_keys(kullanici_ad)
        self.wait_element_visibility(SOYAD).send_keys(kullanici_soyad)
        self.wait_element_visibility(SIFRE).send_keys(valid_password)
        self.driver.execute_script("scrollBy(0,250)")
        time.sleep(2)
        self.wait_element_visibility(SIFRETEKRAR).send_keys(valid_password)
        self.wait_element_visibility(EPOSTA).send_keys("123")
        self.wait_element_visibility(KAYITOL).click()
        time.sleep(30) #CAPTCHA alanlarini gecebilmek icin verildi.
    
    def bos_eposta_uyari_mesaji_kontrolu(self): 
        uyari_masaji = self.wait_element_visibility(EPOSTABOS_UYARIMESAJI)
        return uyari_masaji.text 
    
    def sifre_tekrari_yalnis_doldurulur(self):
        self.wait_element_visibility(ILKKAYITOL).click()
        self.wait_element_visibility(AD).send_keys(kullanici_ad)
        self.wait_element_visibility(SOYAD).send_keys(kullanici_soyad)
        self.wait_element_visibility(EPOSTA).send_keys(kullanici_eposta)
        self.wait_element_visibility(SIFRE).send_keys(valid_password)
        self.driver.execute_script("scrollBy(0,500)")
        time.sleep(20) #CAPTCHA alanlarini gecebilmek icin verildi.
        self.wait_element_visibility(SIFRETEKRAR).send_keys("1")
        self.wait_element_visibility(KAYITOL).click()
        
    def sifre_eslesmedi_popup_kontrolu(self):
        zorunlu_alan = self.wait_element_visibility(YALNIS_SIFRE_POPUP_XPATH)
        return zorunlu_alan.text
    
        
    def mevcut_eposta_ile_kayit(self):
        self.wait_element_visibility(ILKKAYITOL).click()
        self.wait_element_visibility(AD).send_keys(kullanici_ad)
        self.wait_element_visibility(SOYAD).send_keys(kullanici_soyad)
        self.wait_element_visibility(EPOSTA).send_keys("tobeto.0001@gmail.com")
        self.wait_element_visibility(SIFRE).send_keys(valid_password)
        self.driver.execute_script("scrollBy(0,500)")
        time.sleep(20) #CAPTCHA alanlarini gecebilmek icin verildi.
        self.wait_element_visibility(SIFRETEKRAR).send_keys(valid_password)
        self.wait_element_visibility(KAYITOL).click()
        
    def mevcut_eposta_popup_kontrolu(self):
        mevcut_sifre_popup = self.wait_element_visibility(MEVCUTSIFRE_POPUP_XPATH)
        return mevcut_sifre_popup.text
        
        
    def uzun_telNo_ile_sozlesmeler_sayfasini_doldurulur(self): 
        self.wait_element_visibility(ACIKRIZAMETNİ).click()
        self.wait_element_visibility(UYELİKSOZLESMESİ).click()
        self.wait_element_visibility(EPOSTAIZNI).click()
        arama_izni = self.wait_element_visibility(ARAMAIZNI)
        arama_izni.click()
        telno_yaz =self.wait_element_visibility(TELNO)
        telno_yaz.send_keys("123456878901234")
        time.sleep(30) #CAPTCHA alanlarini gecebilmek icin verildi.
        self.wait_element_visibility(DEVAMETBUTTON).click()
     
    def uzun_telNo_uyarisi_kontrolu(self):
        uzun_eposta_uyarisi = self.wait_element_visibility(UZUN_TELNO_UYARISI_XPATH)
        return uzun_eposta_uyarisi.text   
    
    def kisa_telNo_ile_sozlesmeler_sayfasini_doldurulur(self): 
        self.wait_element_visibility(ACIKRIZAMETNİ).click()
        self.wait_element_visibility(UYELİKSOZLESMESİ).click()
        self.wait_element_visibility(EPOSTAIZNI).click()
        arama_izni = self.wait_element_visibility(ARAMAIZNI)
        arama_izni.click()
        telno_yaz =self.wait_element_visibility(TELNO)
        telno_yaz.send_keys("1")
        time.sleep(30)  #CAPTCHA alanlarini gecebilmek icin verildi.
        self.wait_element_visibility(DEVAMETBUTTON).click()
        
    def kisa_telNo_uyarisi_kontrolu(self):
        uzun_eposta_uyarisi = self.wait_element_visibility(KISA_TELNO_XPATH)
        return uzun_eposta_uyarisi.text
    
    def mevcut_telNo_ile_sozlesmeler_sayfasi_doldurulur(self):
        self.wait_element_visibility(ACIKRIZAMETNİ).click()
        self.wait_element_visibility(UYELİKSOZLESMESİ).click()
        self.wait_element_visibility(EPOSTAIZNI).click()
        arama_izni = self.wait_element_visibility(ARAMAIZNI)
        arama_izni.click()
        telno_yaz =self.wait_element_visibility(TELNO)
        telno_yaz.send_keys("5050000000")
        time.sleep(30)  #CAPTCHA alanlarini gecebilmek icin verildi.
        self.wait_element_visibility(DEVAMETBUTTON).click()
        
    def mevcut_telNo_uyarisi_kontrolu(self):
        actual_telNo_uyarisi = self.wait_element_visibility(GORULECEKTEXT_LOCATE)
        return actual_telNo_uyarisi.text
        
    def is_koyitOl_button_enabled(self):
        kayit_olB = self.wait_element_visibility(KAYITOL)
        return kayit_olB.is_enabled()
        