from selenium.webdriver.common.by import By
MEDYA_HESAPLARIM_BUTTON = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-3 mb-8 mb-lg-0']/div/a[6]/span[@class='sidebar-text']")
MEDYA_ACILIR_MENU = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']")
INSTAGRAM_SEC = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[2]")
SEND_URL = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//input[@name='socialMediaUrl']")
URL = "https://www.instagram.com/"
SAVE_SOCIALMEDIA = (By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form/button[.='Kaydet']")
BASARILI_POPUP = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
BASARILI_POPUP_TEXT = "• Sosyal medya adresiniz başarıyla eklendi."

BLANK_AREA_CSS = (By.CSS_SELECTOR, ".text-danger")
BLANK_AREA_TEXT = "Doldurulması zorunlu alan*"

MEDIA_DELETE_BUTTON_XPATH = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//btn[@class='btn social-delete']")
MEDIA_DELETE_CONFIRM_XPATH = (By.XPATH, "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']")

MEDIA_DELETE_POPUP_XPATH = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
MEDIA_DELETE_POPUP_TEXT = ("• Sosyal medya adresiniz başarıyla kaldırıldı.")


MEDIA_UPDATE_BUTTON_XPATH = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//i[@class='fa fa-pencil-square']")
MEDIA_ACILIR_MENU_XPATH = (By.XPATH, "/html/body/div[@role='dialog']/div//form//select")
MEDIA_TWITTER_XPATH = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/form/div/div[1]/select/option[3]")
MEDIA_SEND_URL_XPATH = (By.XPATH, "/html/body/div[@role='dialog']/div//form//input[@value='https://www.instagram.com/']")
URL_TWITTER = "https://www.twitter.com/"
MEDIA_UPDATE_BUTTON = (By.XPATH, "/html/body/div[@role='dialog']//div[@class='modal-footer']/button[1]")
MEDIA_UPDATE_POPUP = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
MEDIA_UPDATE_SUCCESS_TEXT = "Başarıyla güncellendi."

MEDIA_INFO_MESSAGE_CSS = (By.CSS_SELECTOR, ".col-12.col-lg-9 > span")
MEDIA_INFO_MESSAGE_TEXT = "En fazla 3 adet medya seçimi yapılabilir."
ADD_MEDIA_SCRRENSHOT_PATH = r'screenshots/SocialMedia/social-media-added-list.png'
UPDATE_MEDIA_SCRRENSHOT_PATH = r'screenshots/SocialMedia/social-media-update.png'







