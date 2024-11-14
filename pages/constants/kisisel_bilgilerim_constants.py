from selenium.webdriver.common.by import By
import random

# URLs
GIRIS_URL = "https://tobeto.com/giris"
KAYITOL_URL = "https://tobeto.com/kayit-ol"
BASARILIGIRIS_URL = "https://tobeto.com/e-posta-dogrulama?registerType=registerForm"

# Main buttons and navigation
PROFILI_OLUSTUR_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.w-100")
ANASAYFA_BUTTON = (By.CSS_SELECTOR, ".nav-link.c-gray-3")
KULLANICI_ADI_BUTTON = (By.CSS_SELECTOR, "div.navbar-user button")
PROFIL_BILGILERI_BUTTON = (By.CSS_SELECTOR, "div.navbar-user ul li a[href*='profile']")
SOL_MENU = (By.CSS_SELECTOR, ".sidebar-text")

# Form fields
AD_FIELD = (By.NAME, "firstName")
SOYAD_FIELD = (By.NAME, "lastName")
EPOSTA_FIELD = (By.NAME, "email")
SIFRE_FIELD = (By.NAME, "password")
SIFRETEKRAR_FIELD = (By.NAME, "passwordAgain")
TELNO_FIELD = (By.ID, "phoneNumber")
TC_KIMLIK_FIELD = (By.XPATH, "//input[@type='text' and @maxlength='11']")  

# Dropdown selections
ULKE_TEXT = (By.CSS_SELECTOR, "form label[for='country']")
BAYRAK_BUTTON = (By.CSS_SELECTOR, ".flag-button")  
TURKIYE_BAYRAGI = (By.XPATH, "//select/option[@value='225']")
IL_MENU = (By.NAME, "city")
ILCE_MENU = (By.NAME, "district")
IL_ISTANBUL_OPTION = (By.XPATH, "//select[@name='city']/option[text()='Istanbul']")
ILCE_BEYLIKDUZU_OPTION = (By.XPATH, "//select[@name='district']/option[text()='Beylikdüzü']")

# Warnings and alerts
ZORUNLU_FIELD_WARNING1 = (By.XPATH, "//form/p[contains(text(), 'zorunlu alan')]")
ZORUNLU_FIELD_WARNING2 = (By.XPATH, "//form/p[contains(text(), 'zorunlu alan')]")
EPOSTABOS_UYARIMESAJI = (By.XPATH, "//p[contains(text(), 'Geçersiz e-posta adresi')]")
YALNIS_SIFRE_WARNING = (By.XPATH, "//div[@role='dialog' and contains(text(), 'Şifreler Eşleşmedi')]")
MEVCUTSIFRE_WARNING = (By.XPATH, "//div[@role='dialog' and contains(text(), 'kayitli uyelik bulunmaktadir')]")
UZUN_TELNO_WARNING = (By.XPATH, "//small/p[contains(text(), 'En fazla 10 karakter girebilirsiniz')]")
KISA_TELNO_WARNING = (By.XPATH, "//small/p[contains(text(), 'En az 10 karakter girmelisiniz')]")
MEVCUT_TELNO_WARNING = (By.XPATH, "//p[contains(text(), 'kayitli uyelik bulunmaktadir')]")

# Text area limits
MAHALLE_TEXT_AREA = (By.XPATH, "//textarea[@name='address']")
MAHALLE_WARNING = (By.XPATH, "//span[contains(text(), 'En fazla 200 karakter girebilirsiniz')]")
HAKKIMDA_TEXT_AREA = (By.XPATH, "//textarea[@name='about']")
HAKKIMDA_WARNING = (By.XPATH, "//span[contains(text(), 'En fazla 300 karakter girebilirsiniz')]")

# File upload elements
PP_DUZENLEME_BUTTON = (By.CSS_SELECTOR, "button.edit-profile-picture")
DOSYA_YUKLEME_INPUT = (By.XPATH, "//input[@type='file']")
DOSYA_YUKLE_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Yükle')]")

# Save button
KAYDET_BUTTON = (By.XPATH, "//button[contains(text(), 'Kaydet')]")

# Validation for specific pages and titles
EXPECTED_TITLE = "Kişisel Bilgilerim"
