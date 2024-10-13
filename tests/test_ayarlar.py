from time import sleep
from selenium import webdriver
from pages.ayarlar import *
from pages.kisisel_bilgilerim import *
from pages.deneyimlerim import *
import softest
import pytest
import allure



@pytest.mark.usefixtures("setup")
class TobetoAyarlar(softest.TestCase):

    @allure.title("Boş bilgilerle şifre değiştirme kontrolü")
    def test_empty_password_change(self):
        ayarlar = Ayarlar(self.driver)
        ayarlar.ana_giris()
        ayarlar.sayfayi_asagi_indir()
        ayarlar.profil_olustur_bul_tikla()
        ayarlar.ayarlar_butonuna_tikla()
        ayarlar.eski_sifre_bul_ve_gönder("")
        ayarlar.yeni_sifre_bul_ve_gönder("")
        ayarlar.yeni_sifre_tekrar_bul_ve_gönder("")
        ayarlar.sifremi_degistir_butonunu_bul_tikla()
        actual_value = ayarlar.error_line_bul_döndür()
        self.soft_assert(self.assertEqual, ERROR_LINE_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("En 6 karakter şifre kontrolü")
    def test_5_karakter_password_change(self):
        ayarlar = Ayarlar(self.driver)
        ayarlar.ana_giris()
        ayarlar.sayfayi_asagi_indir()
        ayarlar.profil_olustur_bul_tikla()
        ayarlar.ayarlar_butonuna_tikla()
        ayarlar.eski_sifre_bul_ve_gönder(MEVCUT_SIFRE)
        ayarlar.yeni_sifre_bul_ve_gönder(SIFRE_5_KARAKTER)
        ayarlar.yeni_sifre_tekrar_bul_ve_gönder(SIFRE_5_KARAKTER)
        ayarlar.sifremi_degistir_butonunu_bul_tikla()
        actual_value = ayarlar.toast_mesaji_bul_text_döndür
        self.soft_assert(self.assertEqual, EN_AZ_6_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Eşleşmeyen şifre kontrolü")
    def test_eslesmeyen_password_change(self):
        ayarlar = Ayarlar(self.driver)
        ayarlar.ana_giris()
        ayarlar.sayfayi_asagi_indir()
        ayarlar.profil_olustur_bul_tikla()
        ayarlar.ayarlar_butonuna_tikla()
        ayarlar.eski_sifre_bul_ve_gönder(MEVCUT_SIFRE)
        ayarlar.yeni_sifre_bul_ve_gönder(SIFRE_5_KARAKTER)
        ayarlar.yeni_sifre_tekrar_bul_ve_gönder(MEVCUT_SIFRE_2)
        ayarlar.sifremi_degistir_butonunu_bul_tikla()
        actual_value = ayarlar.toast_mesaji_bul_text_döndür
        self.soft_assert(self.assertEqual, SIFRE_ESLESMEDI_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Aynı şifre ile şifre değiştirme kontrolü")
    def test_mevcut_yeni_password_change(self):
        ayarlar = Ayarlar(self.driver)
        ayarlar.ana_giris()
        ayarlar.sayfayi_asagi_indir()
        ayarlar.profil_olustur_bul_tikla()
        ayarlar.ayarlar_butonuna_tikla()
        ayarlar.eski_sifre_bul_ve_gönder(MEVCUT_SIFRE)
        ayarlar.yeni_sifre_bul_ve_gönder(MEVCUT_SIFRE)
        ayarlar.yeni_sifre_tekrar_bul_ve_gönder(MEVCUT_SIFRE)
        ayarlar.sifremi_degistir_butonunu_bul_tikla()
        actual_value = ayarlar.toast_mesaji_bul_text_döndür
        self.soft_assert(self.assertEqual, YENI_SIFRE_MEVCUT_SIFRE_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Başarılı şifre değiştirme kontrolü")
    def test_basarili_password_change(self):
        ayarlar = Ayarlar(self.driver)
        ayarlar.ana_giris()
        ayarlar.sayfayi_asagi_indir()
        ayarlar.profil_olustur_bul_tikla()
        ayarlar.ayarlar_butonuna_tikla()
        ayarlar.eski_sifre_bul_ve_gönder(MEVCUT_SIFRE)
        ayarlar.yeni_sifre_bul_ve_gönder(MEVCUT_SIFRE_2)
        ayarlar.yeni_sifre_tekrar_bul_ve_gönder(MEVCUT_SIFRE_2)
        ayarlar.sifremi_degistir_butonunu_bul_tikla()
        actual_value = ayarlar.toast_mesaji_bul_text_döndür
        self.soft_assert(self.assertEqual, SIFRE_GUNCELLENDI_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Üyeliği sonladır kısmının kontrolü")
    def test_üyeligi_sonlandir(self):
        ayarlar = Ayarlar(self.driver)
        ayarlar.ana_giris()
        ayarlar.sayfayi_asagi_indir()
        ayarlar.profil_olustur_bul_tikla()
        ayarlar.ayarlar_butonuna_tikla()
        ayarlar.üyeligi_sonlandir_butonunu_bul_tikla()
        alert_message = ayarlar.alert_mesaji_bul_döndür()
        hayir = ayarlar.hayir_butonu_bul_döndür()
        evet = ayarlar.evet_butonu_bul_döndür()
        self.soft_assert(self.assertEqual, ALERT_MESSAGE_TEXT , alert_message , "HATA!!!")
        self.soft_assert(self.assertEqual, HAYIR_TEXT , hayir , "HATA!!!")
        self.soft_assert(self.assertEqual, EVET_TEXT , evet , "HATA!!!")
        self.assert_all
