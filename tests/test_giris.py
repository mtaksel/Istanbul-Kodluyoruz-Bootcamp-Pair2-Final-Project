from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.giris import *
from utilities.excel_okuyucu import ExcelOkuyucu
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestTobetoGiris(softest.TestCase, unittest.TestCase):

    # @pytest.fixture(autouse=True)
    # def class_setup(self):
    #     self.giris_sayfasi = Giris(self.driver)

    @allure.title("Başarılı giriş kontrolü")
    @pytest.mark.smoke 
    def test_valid_login(self):
        self.giris_sayfasi = Giris(self.driver)
        self.giris_sayfasi.username_bul_ve_gönder(GIRISMAIL)
        self.giris_sayfasi.password_bul_ve_gönder(GIRISSIFRE)
        self.giris_sayfasi.giris_yap_butonuna_tikla()
        actual_value = self.giris_sayfasi.toast_mesaji_bul_text_döndür()
        self.soft_assert(self.assertEqual, BASARILI_POPUP_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Başarısız giriş kontrolü")
    @pytest.mark.smoke 
    def test_invalid_login(self):
        self.giris_sayfasi = Giris(self.driver)
        self.giris_sayfasi.username_bul_ve_gönder(GECERSIZMAIL)
        self.giris_sayfasi.password_bul_ve_gönder(GECERSIZSIFRE)
        self.giris_sayfasi.giris_yap_butonuna_tikla()
        actual_value = self.giris_sayfasi.toast_mesaji_bul_text_döndür()
        self.soft_assert(self.assertEqual, GECERSIZ_POPUP_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Bilgi kısmını boş bırakarak giriş kontrolü")
    @pytest.mark.smoke 
    def test_empty_login(self):
        self.giris_sayfasi = Giris(self.driver)
        self.giris_sayfasi.username_bul_ve_gönder("")
        self.giris_sayfasi.password_bul_ve_gönder("")
        self.giris_sayfasi.giris_yap_butonuna_tikla()
        actual_value = self.giris_sayfasi.hata_satirlarini_bul_ve_döndür() # Tuple olarak return ettiğimiz değerleri bir değişkene atadık
        expected_value = (BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT) # Return ettiğimiz değerler tuple olduğu için karşılaştırmak istediğimiz değerleri de tuple olarak yazıp bir değişkene atadık
        self.assertTupleEqual(actual_value, expected_value) # Unittest bulunan assertTupleEqual ile tuple değerleri atadığımız değişkenleri assert ettik

    @allure.title("Aktifleştirilmemiş email ile giriş kontrolü")
    @pytest.mark.smoke 
    def test_nonactive_login(self):
        self.giris_sayfasi = Giris(self.driver)
        self.giris_sayfasi.username_bul_ve_gönder(AKTIFOLMAYANMAIL)
        self.giris_sayfasi.password_bul_ve_gönder(AKTIFOLMAYANSIFRE)
        self.giris_sayfasi.giris_yap_butonuna_tikla()
        actual_value = self.giris_sayfasi.toast_mesaji_bul_text_döndür()
        self.soft_assert(self.assertEqual, AKTIFOLMAYAN_POPUP_TEXT , actual_value, "HATA!!!")
        self.assert_all

    @allure.title("Excelden data çekerek başarılı ve başarısız giriş kontrolü")
    @data(*ExcelOkuyucu.excel_verilerini_listeye_cevir(EXCEL_FOLDER, "Sheet1"))
    @unpack
    def test_valid_and_invalid_login(self, email, sifre, expected_value):
        self.giris_sayfasi = Giris(self.driver)
        self.giris_sayfasi.username_bul_ve_gönder(email)
        self.giris_sayfasi.password_bul_ve_gönder(sifre)
        self.giris_sayfasi.giris_yap_butonuna_tikla()
        actual_value = self.giris_sayfasi.toast_mesaji_bul_text_döndür()
        self.soft_assert(self.assertEqual, actual_value, expected_value, "HATA!!!")
        self.assert_all
        

    # def test_valid_login(self):
    #   
    #     #assert self.giris_sayfasi.gecerli_giris() ==  BASARILI_POPUP_TEXT
    #     self.soft_assert(self.assertEqual, BASARILI_POPUP_TEXT , self.giris_sayfasi.gecerli_giris(), "HATA!!!")
    #     self.assert_all

    # def test_invalid_login(self):
    #  
    #     #assert self.giris_sayfasi.gecersiz_giris() == GECERSIZ_POPUP_TEXT
    #     self.soft_assert(self.assertEqual,  GECERSIZ_POPUP_TEXT , self.giris_sayfasi.gecersiz_giris(), "HATA!!!")
    #     self.assert_all

    # def test_empty_login(self):
    #  
    #     #assert self.giris_sayfasi.bos_giris() == BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT
    #     result = self.giris_sayfasi.bos_giris() #Tuple olarak return ettiğimiz değerleri bir değişkene atadık
    #     expected = (BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT) #Return ettiğimiz değerler tuple olduğu için karşılaştırmak istediğimiz değerleri de tuple olarak yazıp bir değişkene atadık
    #     self.assertTupleEqual(result, expected) #Unittest bulunan assertTupleEqual ile tuple değerleri atadığımız değişkenleri assert ettik

        