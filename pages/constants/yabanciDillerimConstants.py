from selenium.webdriver.common.by import By

# Buttons and Links
PROFILIM_BUTTON = (By.CSS_SELECTOR, ".btn.p-0.fw-normal.b-r-35.text-end.d-flex.align-items-center")
PROFIL_BILGILERIM_BUTTON = (By.CSS_SELECTOR, "div.header-avatar > ul > li:nth-child(1) > a")
YABANCIDILLERIM_BUTTON = (By.CLASS_NAME, "languages2")
KAYDET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.py-2.mb-3.d-inline-block.mobil-btn")

# Dropdown Menus and Options
YABANCI_DIL_ACILIR_MENU = (By.NAME, "languageName")
ALMANCA_SEC = (By.XPATH, "//select[@name='languageName']/option[text()='Almanca']")
SEVIYE_SEC_ACILIR_MENU = (By.NAME, "proficiency")
SEVIYE_SEC = (By.XPATH, "//select[@name='proficiency']/option[text()='Option2']")  

# Popups and Messages
SAVE_LANGUAGE_POPUP = (By.CSS_SELECTOR, "div[role='alert'] .toast-body")
DELETE_POPUP = (By.CSS_SELECTOR, "div[role='alert'] .toast-body")
BLANK_MESSAGE = (By.XPATH, "//form/div/div[2]/p")  

# Expected Text
POPUP_MESSAGE_TEXT = "• Yabancı dil bilgisi eklendi."
BLANK_MESSAGE_TEXT = "Doldurulması zorunlu alan*"
DELETE_POPUP_MESSAGE = "• Yabancı dil kaldırıldı."

# Language Deletion
HOVER_ON_LANGUAGE = (By.CSS_SELECTOR, ".col-12.col-lg-9 > div > div > div:nth-child(1)")
DELETE_BUTTON = (By.CSS_SELECTOR, ".col-12.col-lg-9 .delete-lang")
CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[@class='btn btn-yes my-3']")

# Screenshot Paths (If Needed)
ADD_LANGUAGE_SCREENSHOT_PATH = r'screenshots/Language/language-added.png'
DELETE_LANGUAGE_SCREENSHOT_PATH = r'screenshots/Language/language-deleted.png'
