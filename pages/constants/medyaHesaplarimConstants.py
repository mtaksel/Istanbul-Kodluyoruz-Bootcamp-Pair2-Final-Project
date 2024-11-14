from selenium.webdriver.common.by import By

# Buttons and Links
MEDYA_HESAPLARIM_BUTTON = (By.CSS_SELECTOR, "a.sidebar-link:nth-child(6) > span.sidebar-text")
SAVE_SOCIALMEDIA = (By.XPATH, "//button[text()='Kaydet']")
MEDIA_DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.social-delete")
MEDIA_UPDATE_BUTTON = (By.CSS_SELECTOR, ".fa.fa-pencil-square")

# Dropdown Menus and Options
MEDYA_ACILIR_MENU = (By.NAME, "socialMedia")
INSTAGRAM_SEC = (By.XPATH, "//select[@name='socialMedia']/option[text()='Instagram']")
MEDIA_TWITTER_XPATH = (By.XPATH, "//select[@name='socialMedia']/option[text()='Twitter']")

# Input Fields
SEND_URL = (By.NAME, "socialMediaUrl")
MEDIA_SEND_URL = (By.CSS_SELECTOR, "input[value='https://www.instagram.com/']")

# Popups and Messages
BASARILI_POPUP = (By.CSS_SELECTOR, "div[role='alert'] .toast-body")
BLANK_AREA_CSS = (By.CSS_SELECTOR, ".text-danger")
MEDIA_DELETE_CONFIRM = (By.XPATH, "//button[@class='btn btn-yes my-3']")
MEDIA_UPDATE_POPUP = (By.CSS_SELECTOR, "div[role='alert'] .toast-body")
MEDIA_INFO_MESSAGE_CSS = (By.CSS_SELECTOR, ".col-12.col-lg-9 > span")

# Expected Text and URLs
URL = "https://www.instagram.com/"
URL_TWITTER = "https://www.twitter.com/"
BASARILI_POPUP_TEXT = "• Sosyal medya adresiniz başarıyla eklendi."
BLANK_AREA_TEXT = "Doldurulması zorunlu alan*"
MEDIA_DELETE_POPUP_TEXT = "• Sosyal medya adresiniz başarıyla kaldırıldı."
MEDIA_UPDATE_SUCCESS_TEXT = "Başarıyla güncellendi."
MEDIA_INFO_MESSAGE_TEXT = "En fazla 3 adet medya seçimi yapılabilir."

# Screenshots Paths
ADD_MEDIA_SCRRENSHOT_PATH = r'screenshots/SocialMedia/social-media-added-list.png'
UPDATE_MEDIA_SCRRENSHOT_PATH = r'screenshots/SocialMedia/social-media-update.png'
