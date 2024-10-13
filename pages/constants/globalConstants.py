from selenium.webdriver.common.by import By

BASE_URL = "https://tobeto.com/giris"
#Giris yap sayfası giris yap button (CLASSNAME)
GIRISYAPBUTTON = "btn.btn-primary.w-100.mt-6"
USERNAME_LOCATED =  (By.NAME, "email")
PASSWORD_LOCATED = (By.NAME, "password")
BASARILIPOPUP = (By.CSS_SELECTOR, ".toast-body")
#Giris yap sayfası
BASARILI_POPUP_TEXT = "• Giriş başarılı."
