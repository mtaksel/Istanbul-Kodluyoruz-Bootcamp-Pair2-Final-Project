import time
import pytest
from selenium import webdriver
from pages.kisisel_bilgilerim import *
from pages.giris import *
from pages.PageBase import PageBase
import softest
import allure

@pytest.mark.usefixtures("setup")
class TestTobetoKisisel(softest.TestCase,PageBase):

    @allure.title("Kisisel Bilgilerim sayfasının arayüz kontrolü")
    def test_kisisel_bilgilerim_arayuz_kontrolu(self):
        
        page_base=PageBase(self.driver) 
        giris_yap = Giris(self.driver)
        profil_olustur = kisisel_bilgiler(self.driver) 
        
        giris_yap.ana_giris()
        time.sleep(2)
        profil_olustur.sayfayi_asagi_indir()
        profil_olustur.profil_olustur_butonuna_tikla()
        self.soft_assert(self.assertEqual,EXPECTED_TITLE,page_base.get_title(), "Title Hatali!!") #kişisel bilgilerim sayfasında olduğunu titledan doğrular
        self.assert_all()
        profil_olustur.anasayfa_butonuna_tikla()
        profil_olustur.kullanici_adi_butonuna_tikla()  #sağ üstdeki kullanıcı profili butonuna tıklar
        profil_olustur.kullanici_adi_menusundeki_profil_bilgilerine_tikla() #menuden p.bilgilerim seçeneğine tıklar
        actual_result = self.webelement_listesinden_string_listesi_ver(SOL_MENU_LOCATED)
        self.soft_assert(self.assertEqual,profil_olustur.sol_menude_goruntule(),actual_result,"Sol Menu Texti Hatalı!!") #sol menüdeki bölümlerin varlığını doğrular
        self.assert_all()
        actual_ulke_text = self.wait_element_visibility(ULKE_TEXT_LOCATED)
        self.soft_assert(self.assertEqual,profil_olustur.ulke_bolumunde_yildiz_goruntulen(),actual_ulke_text.text, "Ülke kısmında * yok") #Ülke zorunlu alanındaki * lari kontrol eder
        self.assert_all()
        time.sleep(3)
        self.soft_assert(self.assertEqual,KAYITLI_TEL_NO,profil_olustur.kayitli_tel_dogrulama(), "kayit olurken girilen veriyle ayni degil") #kayitli olan telefon numarasiyla yazani kontrol eder.
        self.assert_all
        profil_olustur.bayrak_butonuna_tikla() 
        profil_olustur.bayrak_sec() #menuden bir bayrak secer
        sleep(1)
        profil_olustur.telefon_no_gir() 
        sleep(2)
        profil_olustur.foto_cek() ## dogum günü formatı ve bayrağın fotoğrafı kontrolunu ekran görüntüsü alarak gerçekleştirir        
        self.soft_assert(self.assertEqual,KAYITLI_AD,profil_olustur.kayitli_isim_dogrulama(), "kayit olurken girilen veriyle ayni degil") #kayit olurken girilen isim eşitliğini kontrol eder.
        self.assert_all()
        self.soft_assert(self.assertEqual,profil_olustur.kayitli_soyadi_dogrulama(),KAYITLI_SOYAD, "kayit olurken girilen veriyle ayni degil") #kayit olurken girilen soyad eşitliğini kontrol eder.
        self.assert_all()
        self.soft_assert(self.assertEqual,profil_olustur.kayitli_mail_dogrulama(),KAYITLI_MAIL, "kayit olurken girilen veriyle ayni degil") #kayit olurken girilen mail eşitliğini kontrol eder.
        self.assert_all()
        profil_olustur.il_ilce_liste_kontrolu()
    
    @allure.title("Profil fotoğrafının değiştirilmesi")
    def test_profil_fotografi_degisitirmesi(self):
        
        page_base=PageBase(self.driver) 
        giris_yap = Giris(self.driver)
        profil_olustur = kisisel_bilgiler(self.driver) 
        
        giris_yap.ana_giris()
        time.sleep(3)
        profil_olustur.sayfayi_asagi_indir()
        profil_olustur.profil_olustur_butonuna_tikla()
        profil_olustur.dosya_duzenleme_butonuna_tikla()
        self.soft_assert(self.assertEqual, profil_olustur.pop_up_metinini_goruntule() , DOSYA_YUKLEME_ILK_TEXT , " pop-up mesajı görüntülenemedi")
        self.soft_assert(self.assertEqual, profil_olustur.gozat_butonunu_ve_mesaji_goruntule() , GOZAT_TEXT, "12")
        self.assert_all()
        time.sleep(3)
        file_path = ressm
        upload = self.driver.find_element(By.XPATH, resimadres).send_keys(file_path)
        profil_olustur.dosyayi_yukle_butonuna_tikla()        
        time.sleep(10)
        profil_olustur.foto_cek2()

    @allure.title("Doldurulması zorunlu alanların kontrolü")
    def test_doldurulmasi_zorunlu_alanlarin_kontrolu(self):

        page_base=PageBase(self.driver) 
        giris_yap = Giris(self.driver)
        profil_olustur = kisisel_bilgiler(self.driver) 
        
        giris_yap.ana_giris()
        time.sleep(3)
        profil_olustur.sayfayi_asagi_indir()
        profil_olustur.profil_olustur_butonuna_tikla()
        profil_olustur.sayfayi_asagi_indir()
        time.sleep(3)
        profil_olustur.mahalle_text_gir()
        profil_olustur.hakkimda_text_gir()
        profil_olustur.kaydet_butonuna_tikla()
        profil_olustur.sayfayi_asagi_indir()
        time.sleep(2)
        self.soft_assert(self.assertEqual, profil_olustur.mahalle_uyari_alani(),MAHALLE_UYARI_TEXT, "Uyari mesaji goruntulenemedi")
        self.soft_assert(self.assertEqual, profil_olustur.hakkimda_uyari_alani(),HAKKIMDA_UYARI_TEXT, "Uyari mesaji goruntulenemedi")
        self.assert_all()
    
    @allure.title("TC kimlik alanına geçersiz karakter girilmesi")
    def test_tc_kimlik_gecersiz_karakter_girme(self):

        page_base=PageBase(self.driver) 
        giris_yap = Giris(self.driver)
        profil_olustur = kisisel_bilgiler(self.driver) 
        
        giris_yap.ana_giris()
        time.sleep(5)
        profil_olustur.kullanici_adi_butonuna_tikla()
        profil_olustur.kullanici_adi_menusundeki_profil_bilgilerine_tikla()
        profil_olustur.gecersiz_tc_kimlik_no_gir()
        self.soft_assert(self.assertEqual, profil_olustur.kimlikno_alani,EXPECTED_TEXT, "")
        self.assert_all()
        
        time.sleep(2)
    
    @allure.title("TC kimlik alanına fazla karakter girilmesi")
    def test_tc_kimlik_onbir_haneden_fazla_karakter_girme(self):

        page_base=PageBase(self.driver) 
        giris_yap = Giris(self.driver)
        profil_olustur = kisisel_bilgiler(self.driver) 
        
        giris_yap.ana_giris()
        time.sleep(5)
        profil_olustur.kullanici_adi_butonuna_tikla()
        profil_olustur.kullanici_adi_menusundeki_profil_bilgilerine_tikla()
        profil_olustur.oniki_haneli_tc_kimlik_no_gir()
        profil_olustur.sayfayi_asagi_indir()
        time.sleep(2)
        profil_olustur.kaydet_butonuna_tikla()
        self.soft_assert(self.assertEqual,profil_olustur.tc_kimlik_uyari_alani(),TC_KIMLIK_FAZLA_KARAKTER_UYARI_TEXT, "Uyari mesaji goruntulenemedi")
        self.assert_all()
        time.sleep(2)

        


        

        

        