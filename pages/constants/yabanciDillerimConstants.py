from selenium.webdriver.common.by import By
#Yabancı Dillerim
PROFILIMBUTTON = (By.CLASS_NAME, "btn.p-0.fw-normal.b-r-35.text-end.d-flex.align-items-center")
PROFILBILGILERIMBUTTON = (By.CSS_SELECTOR, "#__next > div > nav > div.container-fluid > div > div > div.btn-group.header-avatar > ul > li:nth-child(1) > a")
YABANCIDILLERIM_BUTTON = (By.CLASS_NAME, "languages2")
YABANCIDIL_ACILIRMENU = (By.NAME, "languageName")
ALMANCASEC = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]")
SEVIYESEC_ACILIRMENU = (By.NAME, "proficiency")
SEVIYESEC =(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/select/option[2]")
KAYDET_BUTTON = (By.CLASS_NAME, "btn.btn-primary.py-2.mb-3.d-inline-block.mobil-btn")

SAVE_LANGUAGE_POPUP_XPATH = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")

#olumlu mesaj
POPUP_MESSAGE_TEXT = "• Yabancı dil bilgisi eklendi."

#doldurulması zorunlu alan uyarı mesajı
BLANK_MESSAGE_TEXT = "Doldurulması zorunlu alan*"

#Yabancı dil silme pop-up mesajı
DELETE_POPUP_MESSAGE = "• Yabancı dil kaldırıldı."

BLANK_MESSAGE = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/p")
HOVER_ON_LAGNGUAGE = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/div/div/div[1]")
DELETE_BUTTON_XPATH = (By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/div/div/div[1]/span[@class='delete-lang']")
CONFIRM_DELETE_XPATH = (By.XPATH, "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']")
DELETE_POPUP_XPATH = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")

