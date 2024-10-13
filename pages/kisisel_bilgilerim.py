import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.kisisel_bilgilerim_constants import *
from pages.giris import Giris
from time import sleep
import re

@pytest.mark.usefixtures("setup")
class kisisel_bilgiler(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def profil_olustur_butonuna_tikla(self):
        sleep(1)
        profil_olustur_butonu = self.wait_element_visibility(PROFILI_OLUSTUR_BUTTON_LOCATED)
        profil_olustur_butonu.click()
        sleep(4)

    def sayfayi_asagi_indir(self):
        self.driver.execute_script("scrollBy(0,1000)")

    def get_title(self):
        return self.driver.title
    
    def anasayfa_butonuna_tikla(self):
        anasayfa_butonu = self.wait_element_visibility(ANASAYFA_BUTONU_LOCATED)
        anasayfa_butonu.click()

    def kullanici_adi_butonuna_tikla(self):
        kullanici_adi_butonu = self.wait_element_visibility(KULLANICI_ADI_BUTONU_LOCATED)
        kullanici_adi_butonu.click()
        sleep(2)

    def kullanici_adi_menusundeki_profil_bilgilerine_tikla(self):
        profil_bilgileri_butonu = self.wait_element_visibility(PROFIL_BILGILERI_LOCATED)
        profil_bilgileri_butonu.click()
        sleep(2)
    
    def sol_menude_goruntule(self):
        expected_sol_menu = ["Kişisel Bilgilerim", "Deneyimlerim", "Eğitim Hayatım", "Yetkinliklerim", "Sertifikalarım", "Medya Hesaplarım", "Yabancı Dillerim", "Ayarlar"]
        return expected_sol_menu 
    
    def ulke_bolumunde_yildiz_goruntulen(self):
        ulke_bolumu = "Ülke*"
        return ulke_bolumu
    
    def foto_cek(self):
        screenshot_path = SCREENSHOT1
        self.driver.save_screenshot(screenshot_path)

    def foto_cek2(self):
        screenshot_path = SCREENSHOT2
        self.driver.save_screenshot(screenshot_path)

    def bayrak_butonuna_tikla(self):
        self.wait_element_visibility(BAYRAK_BUTON_LOCATED).click()
    
    def bayrak_sec(self):
        self.wait_element_visibility(BAYRAK_SEC_LOCATED).click()
    
    def telefon_no_gir(self):
        telefon_no = self.wait_element_visibility(TELEFON_NO_LOCATED)
        telefon_no.send_keys(TELEFON_NO_DATA)
    
    def kayitli_isim_dogrulama(self):
        isim = self.wait_element_visibility(KSB_AD_LOCATE)
        isim_value = isim.get_attribute("value")
        return isim_value
    
    def kayitli_soyadi_dogrulama(self):
        soyadi = self.wait_element_visibility(KSB_SOYAD_LOCATE)
        soyadi_value = soyadi.get_attribute("value")
        return soyadi_value
    
    def kayitli_mail_dogrulama(self):
        mail = self.wait_element_visibility(KSB_MAIL_LOCATE)
        self.driver.execute_script("arguments[0].removeAttribute('disabled');", mail)
        mail_value = mail.get_attribute("value")
        return mail_value
    
    def kayitli_tel_dogrulama(self):
        tel = self.wait_element_visibility(KSB_TEL_NO_LOCATE)
        tel_value = tel.get_attribute("value")
        return tel_value
    
    def il_ilce_liste_kontrolu(self):
        il_dropdown_menu = self.wait_element_visibility(IL_MENU_LOCATE)
        il_dropdown_menu.click()
        ilce_sec = self.wait_element_visibility(IL_ISTANBUL_PATH)
        ilce_sec.click()
        ilce_dropdown_menu = self.wait_element_visibility(ILCE_MENU_LOCATE)
        ilce_dropdown_menu.click()
        ilce_sec = self.wait_element_visibility(ILCE_BEYLIKDUZU_PATH)
        ilce_sec.click()

#####################

    def dosya_duzenleme_butonuna_tikla(self):
        dosya_duzenleme_butonu = self.wait_element_visibility(PP_DUZENLEME_BUTON_LOCATE)
        dosya_duzenleme_butonu.click()
    
    def pop_up_metinini_goruntule(self):
        pop_up_metini = self.wait_element_visibility(DOSYA_YUKLEME_ILK_LOCATE)
        return pop_up_metini.text
    
    def gozat_butonunu_ve_mesaji_goruntule(self):
        gozat_butonu_mesaj = self.wait_element_visibility(GOZAT_LOCATE)
        return gozat_butonu_mesaj.text
    
    #def resim_yukle(self):
    #       file_upload = self.driver.find_element(GOZAT_BUTON_LOCATE).send_keys(DOSYA1_PATH)

    def dosyayi_yukle_butonuna_tikla(self):
        dosya_yukle_butonu = self.wait_element_visibility(DOSYA_SUBMIT_LOCATE)
        dosya_yukle_butonu.click()

    def mahalle_text_gir(self):
        mahalle_text = self.wait_element_visibility(MAHALLE_TEXT_LOCATE)
        mahalle_text.send_keys(IKIYUZ_KARAKTERLI_TEXT)
    
    def hakkimda_text_gir(self):
        hakkimda_text = self.wait_element_visibility(HAKKIMDA_TEXT_LOCATE)
        hakkimda_text.send_keys(UCYUZ_KARAKTERLI_TEXT)


    def kaydet_butonuna_tikla(self):
        kaydet_butonu = self.wait_element_visibility(KAYDET_BUTON_LOCATE)
        kaydet_butonu.click()

    def mahalle_uyari_alani(self):
        mahalle_uyari = self.wait_element_visibility(MAHALLE_UYARI_TEXT_LOCATE)
        return mahalle_uyari.text

    def hakkimda_uyari_alani(self):
        hakkimda_uyari = self.wait_element_visibility(HAKKIMDA_UYARI_TEXT_LOCATE)
        return hakkimda_uyari.text
    
    #####################
     
    def kimlikno_alani(self):
        tc_kimlik = self.wait_element_visibility(TC_KIMLIK_LOCATED)
        tc_kimlikvalue = tc_kimlik.get_attribute("value")
        return tc_kimlikvalue

    def gecersiz_tc_kimlik_no_gir(self):
        tc_kimlik = self.wait_element_visibility(TC_KIMLIK_LOCATED)
        tc_kimlik.send_keys(GECERSIZ_TC_KIMLIK_DATA)

    def oniki_haneli_tc_kimlik_no_gir(self):
        tc_kimlik = self.wait_element_visibility(TC_KIMLIK_LOCATED)
        tc_kimlik.send_keys(ONIKI_HANELI_TC_KIMLIK)

    def tc_kimlik_uyari_alani(self):
        tc_uyari_alan = self.wait_element_visibility(TC_KIMLIK_UYARI_LOCATED)
        return tc_uyari_alan.text
       
    ### def gecersiz_karakter_kontrolu(self):
    ###   x = re.findall("[+]", GECERSIZ_TC_KIMLIK_DATA)
    ###    print(x)