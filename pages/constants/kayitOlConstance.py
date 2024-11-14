from selenium.webdriver.common.by import By
import random

KAYITOLBUTTON = (By.CSS_SELECTOR, ".text-decoration-none.text-muted.fw-bold")

GIRIS_URL = "https://tobeto.com/giris"
KAYITOL_URL = "https://tobeto.com/kayit-ol"

# Kayit ol sayfasi
AD = (By.NAME, "firstName")
SOYAD = (By.NAME, "lastName")
EPOSTA = (By.NAME, "email")
SIFRE = (By.NAME, "password")
SIFRETEKRAR = (By.NAME, "passwordAgain")
KAYITOL = (By.CSS_SELECTOR, ".btn.btn-primary.w-100.mt-6")

ILKKAYITOL = (By.CSS_SELECTOR, ".text-decoration-none.text-muted.fw-bold")

# Sozlesmeler sayfasi
ACIK_RIZA_METNI = (By.NAME, "contact")
UYELIK_SOZLESMESI = (By.NAME, "membershipContrat")
EPOSTA_IZNI = (By.NAME, "emailConfirmation")
ARAMA_IZNI = (By.NAME, "phoneConfirmation")
TEL_NO = (By.ID, "phoneNumber")
telno = random.randint(1000000000, 9999999999)
ROBOT_DEGILIM = (By.ID, "recaptcha-anchor")
DEVAM_ET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-yes.my-3")

# Valid giris
kullanici_ad = "Tobeto"
kullanici_soyad = "Kodluyor"
randonint = str(random.randint(1000, 9999))
kullanici_eposta = f"tobeto{randonint}@gmail.com"
valid_password = "123456"
BASARILI_GIRIS_URL = "https://tobeto.com/e-posta-dogrulama?registerType=registerForm"
TIK_ISARET = (By.XPATH, "//div[@id='__next']//svg/path[1]")
KAYIT_TEXTI = (By.CLASS_NAME, "success-payment-text")
GORULECEK_TEXT_LOCATE = (By.XPATH, "//div[@id='__next']/main/section//div/span")
GORUNECEK_TEXT = "Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."

# Uyari metni: doldurulması zorunlu alan
ZORUNLU1 = (By.XPATH, "//div[@id='__next']//form/p[1]")
ZORUNLU2 = (By.XPATH, "//div[@id='__next']//form/p[2]")

# Bos eposta uyarısı
EPOSTA_BOS_UYARI_MESAJI = (By.XPATH, "//div[@id='__next']//form/p")
BOSEPOSTA_TEXT = "Geçersiz e-posta adresi*"

# Yalnis sifre tekrari
YALNIS_SIFRE_POPUP = (By.XPATH, "//div[@role='dialog']")
YALNIS_SIFRE_POPUP_TEXT = "• Şifreler Eşleşmedi"

# Mevcut eposta ile giris ve sonrasında gorunen popup
MEVCUT_SIFRE_TEXT = "Girdiginiz eposta adresi ile kayitli uyelik bulunmaktadir."
MEVCUT_SIFRE_POPUP = (By.XPATH, "//div[@role='dialog']")

# Uzun tel no uyarısı
UZUN_TELNO_UYARISI = (By.XPATH, "//label[4]/small/p")
UZUN_TELNO_UYARISI_TEXT = "En fazla 10 karakter girebilirsiniz."

# Kısa tel no ile giris
KISA_TELNO = (By.XPATH, "//label[4]/small/p")
KISA_TELNO_TEXT = "En az 10 karakter girmelisiniz."

# Mevcut tel no ile kayit
MEVCUT_TELNO_UYARISI_TEXT = "Girdiginiz telefon numarasi ile kayitli uyelik bulunmaktadir."
