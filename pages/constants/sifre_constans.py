from selenium.webdriver.common.by import By

#Password Locators
SIFREMI_UNUTTUM_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".d-block")
MAIL_INPUT_LOCATOR = (By.CLASS_NAME, "form-control.mt-6")
GONDER_BUTTON_LOCATOR = (By.CLASS_NAME, "btn.btn-primary.w-100.mt-6")
TOAST_MESSAGE_LOCATOR = (By.CLASS_NAME, "toast-body")
GMAIL_MAIL_INPUT_LOCATOR = (By.CSS_SELECTOR, "input[type='email']")
GMAIL_PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, "input[type='password']")
SONRAKI_BUTTON_LOCATOR = (By.XPATH, "//span[text()='Sonraki']")
GMAIL_MAIL_BUL_LOCATOR = (By.XPATH, ".zA[class^='zA'")
GMAIL_SIFIRLAMA_LINK_LOCATOR = (By.XPATH, '//a[contains(@href, "tobeto.com")]')
SIFRE_SIFIRLAMA_INPUT_LOCATOR = (By.XPATH, '//input[@name="password"]')
SIFRE_SIFIRLAMA_INPUT2_LOCATOR = (By.XPATH, '//input[@name="passwordConfirmation"]')

GIRISMAIL = "tobeto.0001@gmail.com"
SIFIRLAMA_MAIL = "tobeto.0003@gmail.com"
SIFIRLAMA_GMAIL_SIFRE = "xwdutzkpnzrugrvh"
SIFIRLAMA_TOBETO_SIFRE = "TestTobeto1234"
SIFRE_SIFIRLAMA_BASARILI_TEXT = "• Şifre sıfırlama işlemi başarılı."
SIFRE_POPUP_TEXT = "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
SIFRE_GECERSIZ_MAIL_POPUP_TEXT = "• Girdiğiniz e-posta geçersizdir."
SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT = "• Kullanıcı bulunamadı."
SCREENSHOT_FOLDER = r"screenshots\password"
GMAIL_INBOX_URL = "https://mail.google.com/mail/u/0/#inbox"


