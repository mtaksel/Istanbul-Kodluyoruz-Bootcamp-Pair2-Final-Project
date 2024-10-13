import pytest
import pyautogui
from selenium import webdriver
from pages.yabanci_dillerim import *
from pages.giris import *
from pages.medyaHesaplarim import *
import softest
import allure

@pytest.mark.usefixtures("setup")
class TestTobetoMedyaHesaplarim(softest.TestCase):
    
    #PASS TEST
    @allure.title("Yeni bir medya hesabı ekleme kontrolü")
    def test_medya_hesabi_ekle(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_ekle(self.driver)
        medya_hesaplarim = Medya_hesabi_ekle(self.driver)
        
        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        medya_hesaplarim.medya_hesaplarima_tikla()
        medya_hesaplarim.medya_acilir_menu_tikla()
        medya_hesaplarim.medya_sec()
        medya_hesaplarim.medya_url_gir()
        medya_hesaplarim.medya_kaydet()
        self.soft_assert(self.assertEqual, BASARILI_POPUP_TEXT, medya_hesaplarim.basarili_kaydetme(), "HATALI MESAJ")
        self.assert_all()

    #PASS TEST
    @allure.title("İlgili alanların boş geçilmesi durumu")
    def test_medya_hesabi_bos_alan_kontrolu(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_ekle(self.driver)
        medya_hesaplarim = Medya_hesabi_bos_alan_kontrolu(self.driver)
        
        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        medya_hesaplarim.medya_hesaplarima_tikla()
        medya_hesaplarim.medya_acilir_menu_tikla()
        medya_hesaplarim.medya_sec()
        medya_hesaplarim.medya_kaydet()
        self.soft_assert(self.assertEqual, BLANK_AREA_TEXT, medya_hesaplarim.bos_alan_kaydetme(), "HATALI MESAJ")
        self.assert_all()

    #PASS TEST AND SCREENSHOT
    @allure.title("Ekli olan medya hesaplarının kontrolü")
    def test_medya_hesabi_liste_kontrolu(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_ekle(self.driver)
        medya_hesaplarim = Eklenen_medya_hesabi_kontrolu(self.driver)
        
        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        medya_hesaplarim.medya_hesaplarima_tikla()
        self.soft_assert(self.assertEqual, MEDIA_INFO_MESSAGE_TEXT, medya_hesaplarim.bilgi_mesaji_goruntule(), "HATALI MESAJ")
        pyautogui.screenshot(ADD_MEDIA_SCRRENSHOT_PATH)
        self.assert_all()

    #PASS TEST 
    @allure.title("Var olan bir medya hesabını silme kontrolü")
    def test_medya_hesabi_silme_islemi(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_ekle(self.driver)
        medya_hesaplarim = Medya_hesabi_silme(self.driver)
        
        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        medya_hesaplarim.medya_hesaplarima_tikla()
        medya_hesaplarim.silme_butonuna_tikla()
        medya_hesaplarim.silme_islemini_onayla()
        self.soft_assert(self.assertEqual, MEDIA_DELETE_POPUP_TEXT, medya_hesaplarim.silme_islemi_basarili(), "HATALI MESAJ")
        self.assert_all()

    
    #FAIL TEST
    @allure.title("Var olan medya hesabını güncelleme işleminin kontrolü")
    def test_medya_hesabi_guncelle(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_ekle(self.driver)
        medya_hesaplarim = Medya_hesabi_guncelle(self.driver)
        
        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        medya_hesaplarim.medya_hesaplarima_tikla()
        medya_hesaplarim.guncelle_butonuna_tikla()
        medya_hesaplarim.acilir_menu_tikla()
        medya_hesaplarim.medya_hesabi_sec()
        medya_hesaplarim.medya_url_gir()
        medya_hesaplarim.medya_guncelle()
        self.soft_assert(self.assertEqual, MEDIA_UPDATE_SUCCESS_TEXT, medya_hesaplarim.guncelleme_islemini_gerceklestir(), "• Forbidden")
        pyautogui.screenshot(UPDATE_MEDIA_SCRRENSHOT_PATH)
        self.assert_all()
        