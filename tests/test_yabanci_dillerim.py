import pytest
from selenium import webdriver
from pages.yabanci_dillerim import *
from pages.PageBase import PageBase
from pages.giris import *
import softest
import allure

@pytest.mark.usefixtures("setup")
class TestTobetoYabanciDillerim(softest.TestCase,PageBase):
    
    @allure.title("Yeni bir dil ekleme kontrolü")
    def test_yabanci_dil_ekle(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_ekle(self.driver) #baska sayfadan cagırılan fonksiyon
        
        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        yabanci_dillerim.yabanci_dillerim_tikla()
        yabanci_dillerim.dil_acilirmenu_tikla()
        yabanci_dillerim.yabancidil_sec()
        yabanci_dillerim.seviye_acilirmenu_tikla()
        yabanci_dillerim.seviye_sec()
        yabanci_dillerim.kaydet()
        self.soft_assert(self.assertEqual, POPUP_MESSAGE_TEXT, yabanci_dillerim.kaydetme_basarili(), "HATALI BASARILI MESAJI")
        self.assert_all()
        

    @allure.title("İlgili alanların boş geçilmesi durumu")
    def test_yabanci_dil_bos_alan_kontrolu(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_bos_gecme(self.driver)

        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        yabanci_dillerim.yabanci_dillerim_tikla()
        yabanci_dillerim.dil_acilirmenu_tikla()
        yabanci_dillerim.yabancidil_sec()
        yabanci_dillerim.seviye_acilirmenu_tikla()
        yabanci_dillerim.kaydet()
        self.soft_assert(self.assertEqual, BLANK_MESSAGE_TEXT, yabanci_dillerim.doldurulmasi_zorunlu_alan_mesaji(), "HATALI MESAJ")
        self.assert_all()

    @allure.title("Yabancı dil silme kontrolü")
    def test_yabanci_dil_silme_kontrolu(self):
        giris = Giris(self.driver)
        yabanci_dillerim = Yabanci_dil_silme(self.driver)

        giris.ana_giris()
        yabanci_dillerim.profilim_kismina_tikla()
        yabanci_dillerim.profil_bilgileri_tikla()
        yabanci_dillerim.yabanci_dillerim_tikla()
        yabanci_dillerim.sil_butonuna_tikla()
        yabanci_dillerim.silmeyi_onayla()
        self.soft_assert(self.assertEqual, DELETE_POPUP_MESSAGE, yabanci_dillerim.silme_islemi_basarili(), "HATALI MESAJ")
        self.assert_all()       


        
        