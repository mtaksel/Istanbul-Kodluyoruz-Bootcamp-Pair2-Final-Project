from selenium.webdriver.common.by import By

PROFILI_OLUSTUR_BUTTON_LOCATED = (By.CLASS_NAME, "btn.btn-primary.w-100")
ANASAYFA_BUTONU_LOCATED = (By.CLASS_NAME, "nav-link.c-gray-3")
KULLANICI_ADI_BUTONU_LOCATED = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")
PROFIL_BILGILERI_LOCATED = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
SOL_MENU_LOCATED = (By.CLASS_NAME, "sidebar-text")
ULKE_TEXT_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/label")
BAYRAK_BUTON_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div")
BAYRAK_SEC_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div/select/option[216]")
TELEFON_NO_LOCATED = (By.XPATH, "//*[@id='phoneNumber']")
TURKIYE_BAYRAGI_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div/select/option[225]")
TC_KIMLIK_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input")

SCREENSHOT1 = r'screenshots\kisisel_bilgilerim\ulke_bayragi_degisimi.png'
SCREENSHOT2 = r'screenshots\kisisel_bilgilerim\profil_bayragi_degisti.png' 

TELEFON_NO_DATA = "+90"
GECERSIZ_TC_KIMLIK_DATA = "+"
EXPECTED_TITLE = "Kişisel Bilgilerim"


KSB_AD_LOCATE = (By.NAME, "name")
KSB_SOYAD_LOCATE = (By.NAME, "surname")
KSB_MAIL_LOCATE = (By.NAME, "email")
KSB_TEL_NO_LOCATE = (By.ID, "phoneNumber")

KAYITLI_AD = "Tobeto"
KAYITLI_SOYAD = "Tobeto"
KAYITLI_MAIL = "tobeto.0001@gmail.com"
KAYITLI_TEL_NO = "+90 505 000 00 00"

IL_MENU_LOCATE = (By.NAME, "city")
ILCE_MENU_LOCATE = (By.NAME, "district")
IL_ISTANBUL_PATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[41]")
ILCE_BEYLIKDUZU_PATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select/option[13]")

PP_DUZENLEME_BUTON_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div[1]")
DOSYA_YUKLEME_ILK_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]")
DOSYA_YUKLEME_ILK_TEXT = ("Sürükleyip bırak, yapıştır veya\ngözat")
GOZAT_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button")
GOZAT_TEXT = ("gözat")
GOZAT_BUTON_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]")
DOSYA1_PATH = r'test_tobeto\uploads\resim1.png'
DOSYA_SUBMIT_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button")

KAYDET_BUTON_LOCATE = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button")

MAHALLE_TEXT_LOCATE = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/textarea")
HAKKIMDA_TEXT_LOCATE = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea")

IKIYUZ_KARAKTERLI_TEXT = "sagittis nibh vitae nunc mollis, sed congue nibh mattis. Nullam a dolor eu nunc vulputate mattis. Suspendisse potenti. Nam nec nisl nec nisl mollis mattis. Nullam a dolor eu nunc vulputate mattis. Susp"

UCYUZ_KARAKTERLI_TEXT = "sagittis nibh vitae nunc mollis, sed congue nibh mattis. Nullam a dolor eu nunc vulputate mattis. Suspendisse potenti. Nam nec nisl nec nisl mollis mattis. Nullam a dolor eu nunc vulputate mattis. Susp Nullam a dolor eu nunc vulputate mattis Nullam a dolor eu nunc vulputate mattis Nullam a dolor eu s"

TC_KIMLIK_BOS_UYARI_TEXT = "*Aboneliklerde fatura için doldurulması zorunlu alan"
TC_KIMLIK_BOS_UYARI_TEXT2 = "Aboneliklerde fatura için doldurulması zorunlu alan"

MAHALLE_UYARI_TEXT = "En fazla 200 karakter girebilirsiniz"
HAKKIMDA_UYARI_TEXT = "En fazla 300 karakter girebilirsiniz"

MAHALLE_UYARI_TEXT_LOCATE = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/span")
HAKKIMDA_UYARI_TEXT_LOCATE = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/span")

ONIKI_HANELI_TC_KIMLIK = "111111111111"

TC_KIMLIK_UYARI_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]")
TC_KIMLIK_FAZLA_KARAKTER_UYARI_TEXT = "TC Kimlik Numarası 11 Haneden Fazla olamaz"

ressm = r'C:\Users\mehme\Desktop\test_tobeto\uploads\resim1.png'
resimadres = "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]"

EXPECTED_TEXT = ""