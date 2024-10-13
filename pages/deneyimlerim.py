import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.deneyimlerimConstants import *
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import datetime 
from pages.giris import Giris


@pytest.mark.usefixtures("setup")

class Deneyimlerim(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def kullanici_isim_butonuna_tikla(self):       
        kullanici_isim_butonu= self.driver.find_element(By.XPATH,KULLANICI_ISIM_BUTONU)
        kullanici_isim_butonu.click()

    def profil_bilgilerim_butonuna_tiklar(self):
        profil_bilgilerim=self.driver.find_element(By.XPATH,PROFIL_BILGILERI_BUTONU)
        profil_bilgilerim.click()

    def deneyimlerim_butonuna_tiklar(self):
        deneyimlerim=self.driver.find_element(By.XPATH, DENEYIMLERIM_BUTONU)
        deneyimlerim.click()

    def kurum_adi_textbox_deger_girer(self):
        kurum_adi_textbox=self.driver.find_element(By.XPATH,KURUM_ADI_TEXTBOX)
        kurum_adi_textbox.send_keys(DATA_KURUM_ADI)    
                  
    def kurum_adi_textbox_gecersiz_deger_girer(self):
        try:
            kurum_adi_textbox=self.driver.find_element(By.XPATH,KURUM_ADI_TEXTBOX)
            kurum_adi_textbox.send_keys(DATA_GECERSIZ_KURUM_ADI)
        except NoSuchElementException:
            print("Kurum adi textbox locate hatalii!!! ")

    def pozisyon_textbox_deger_girer(self):
        pozisyon_adi_textbox=self.driver.find_element(By.XPATH,POZISYON_TEXTBOX)
        pozisyon_adi_textbox.send_keys(DATA_POZISYON)

    def sektor_textbox_deger_girer(self):
        sektor_textbox=self.driver.find_element(By.XPATH, SEKTOR_TEXTBOX)
        sektor_textbox.send_keys(DATA_SEKTOR)
 
    def sehir_seciniz_dropdown_sehir_secimi_yapar(self):
        sehir_secimi_dropdown_located=self.driver.find_element(By.XPATH,SEHIR_SECINIZ_DROPDOWN)
        sehirler = Select(sehir_secimi_dropdown_located)

        #webelement listesini yazdirir
        sehirler_listesi = sehirler.options  # sehirleri webelemen listesi olarak dondurur.
        # for sehir in sehirler_listesi:
        #     print(sehir.text)

        #1. yol
        sehirler.select_by_visible_text(DATA_SEHIR)
        #2. yol
        # sehirler.select_by_index("0") #index 0 dan baslar

    def is_baslangic_tarihine_deger_girer(self):
        is_baslangic_located=self.driver.find_element(By.XPATH,IS_BASLANGIC_TEXTBOX)
        is_baslangic_located.click()
        time.sleep(5)

        is_baslangic_yil_located=self.driver.find_element(By.XPATH,IS_BASLANGIC_YIL)
        yillar=Select(is_baslangic_yil_located)
        yillar.select_by_visible_text(DATA_IS_GIRIS_YILI)
        time.sleep(5)

        is_baslangic_ay_located=self.driver.find_element(By.XPATH,IS_BASLANGIC_AY)
        aylar=Select(is_baslangic_ay_located)
        aylar.select_by_visible_text(DATA_IS_BASLANGIC_AY)
        time.sleep(3)
        self.driver.find_element(By.XPATH,IS_BASLANGIC_GUN).click()

        # tarih=datetime.datetime(2020,1,1)
        # date=tarih.strftime("%d/%m/%Y")
        # is_baslangic_located.send_keys(date)

    def is_bitis_tarihi_deger_girer(self):
        self.driver.find_element(By.XPATH,IS_BITIS_TEXTBOX).click()
        time.sleep(3)
        is_bitis_yil_located=self.driver.find_element(By.XPATH,IS_BITIS_YIL)
        yillar=Select(is_bitis_yil_located)
        yillar.select_by_visible_text(DATA_IS_BITIS_YIL)
        time.sleep(3)
        is_bitis_ay_located=self.driver.find_element(By.XPATH,IS_BITIS_AY)
        aylar=Select(is_bitis_ay_located)
        aylar.select_by_visible_text(DATA_IS_BITIS_AY)
        time.sleep(3)
        self.driver.find_element(By.XPATH,IS_BITIS_GUN).click()

    def calismaya_devam_ediyorum_butonuna_tiklar(self):
        self.driver.find_element(By.XPATH,CALISMAYA_DEVAM_EDIYORUM_BUTONU).click()

    def is_aciklamasi_texbox_deger_girer(self):
        is_aciklamasi_located=self.driver.find_element(By.XPATH,IS_ACIKLAMASI)
        is_aciklamasi_located.send_keys(DATA_IS_ACIKLAMASI)

    def kaydet_butonuna_tiklar(self):
        self.driver.find_element(By.XPATH,KAYDET_BUTONU).click()
        
    def basari_mesaji(self):
        basari_mesaji=self.driver.find_element(By.CLASS_NAME,DENEYIM_EKLENDI_MESAJI)
        return basari_mesaji.text
    
    def eklenen_kurum_adini_dondurur(self):
        kurum_adi=self.driver.find_element(By.XPATH,EKLENEN_KURUM_ADI)
        return kurum_adi.text
    
    def eklenen_pozisyon_dondurur(self):
        pozisyon=self.driver.find_element(By.XPATH,EKLENEN_POZISYON)
        return pozisyon.text
    
    def eklenen_sektor__dondurur(self):
        sektor=self.driver.find_element(By.XPATH,EKLENEN_SEKTOR)
        return sektor.text
    
    def eklenen_sehir_dondurur(self):
        sehir=self.driver.find_element(By.XPATH,EKLENEN_SEHIR)
        return sehir.text
    
    def is_aciklamasi_dondurur(self):
        self.driver.find_element(By.XPATH,UC_NOKTA).click()
        is_aciklamasi=self.driver.find_element(By.XPATH,EKLENEN_IS_ACIKLAMASI)
        return is_aciklamasi.text
    
    def eklenen_tarih_araligini_dondurur(self):
        eklenen_tarih_araligi=self.driver.find_element(By.XPATH,EKLENEN_TARIH_ARALIGI)
        return eklenen_tarih_araligi.text

    def deneyim_sil_butonuna_tiklar(self):
        sil_butonu=self.driver.find_element(By.XPATH,SIL_BUTONU)
        sil_butonu.click()

    def deneyim_sil_evet_butonuna_basar(self):       
        self.driver.find_element(By.XPATH,DENEYIM_SIL_EVET_BUTONU).click()

    def deneyim_sil_hayir_butonuna_basar(self):
        self.driver.find_element(By.XPATH,DENEYIM_SIL_HAYIR_BUTONU).click()

    def deneyim_silindi_mesajini_dondurur(self):
        mesaj=self.driver.find_element(By.XPATH,DENEYIM_KALDIRILDI_MESAJI)
        return mesaj.text
    
    def kurum_adi_hata_mesaji_dondurur(self):
        mesaj=self.wait_element_visibility(KURUM_ADI_DATA_MESAJI)
        return mesaj.text

    def zorunlu_alan_hata_kontrolu(self):
        mesajlar=self.webelement_listesinden_string_listesi_ver(UYARI_MESAJI)
        return len(mesajlar)


        


    
    
    


