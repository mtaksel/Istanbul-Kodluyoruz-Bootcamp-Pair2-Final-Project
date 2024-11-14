from selenium.webdriver.common.by import By

# Button for the user profile in the header navigation
KULLANICI_ISIM_BUTONU = (By.CSS_SELECTOR, "button[data-testid='user-profile-button'] div p")

# Button for profile information
PROFIL_BILGILERI_BUTONU = (By.LINK_TEXT, "Profil Bilgileri")

# Button for experience section
DENEYIMLERIM_BUTONU = (By.PARTIAL_LINK_TEXT, "Deneyimlerim")

# Form fields
KURUM_ADI_TEXTBOX = (By.CSS_SELECTOR, "input[name='institution-name']")
POZISYON_TEXTBOX = (By.CSS_SELECTOR, "input[name='position']")
SEKTOR_TEXTBOX = (By.CSS_SELECTOR, "input[name='sector']")
SEHIR_SECINIZ_DROPDOWN = (By.CSS_SELECTOR, "select[name='city']")
IS_BASLANGIC_TEXTBOX = (By.CSS_SELECTOR, "input[name='start-date']")
IS_BITIS_TEXTBOX = (By.CSS_SELECTOR, "input[name='end-date']")
IS_ACIKLAMASI = (By.TAG_NAME, "textarea")

# Start and end date dropdowns
IS_BASLANGIC_YIL = (By.CSS_SELECTOR, "select[name='start-year']")
IS_BASLANGIC_AY = (By.CSS_SELECTOR, "select[name='start-month']")
IS_BASLANGIC_GUN = (By.CSS_SELECTOR, "select[name='start-day']")
IS_BITIS_YIL = (By.CSS_SELECTOR, "select[name='end-year']")
IS_BITIS_AY = (By.CSS_SELECTOR, "select[name='end-month']")
IS_BITIS_GUN = (By.CSS_SELECTOR, "select[name='end-day']")

# Checkbox for "Currently working"
CALISMAYA_DEVAM_EDIYORUM_BUTONU = (By.CSS_SELECTOR, "input[type='checkbox'][name='currently-working']")

# Save button for the experience section
KAYDET_BUTONU = (By.CSS_SELECTOR, "button[type='submit']")

# Toast message for experience added
DENEYIM_EKLENDI_MESAJI = (By.CLASS_NAME, "toast-body")

# Elements to verify added experience details
EKLENEN_KURUM_ADI = (By.CSS_SELECTOR, "span[data-testid='added-institution']")
EKLENEN_POZISYON = (By.CSS_SELECTOR, "span[data-testid='added-position']")
EKLENEN_SEKTOR = (By.CSS_SELECTOR, "span[data-testid='added-sector']")
EKLENEN_SEHIR = (By.CSS_SELECTOR, "span[data-testid='added-city']")
EKLENEN_IS_ACIKLAMASI = (By.CSS_SELECTOR, "div[data-testid='experience-description']")
EKLENEN_TARIH_ARALIGI = (By.CSS_SELECTOR, "span[data-testid='date-range']")

# Error message for required fields
UYARI_MESAJI = (By.CLASS_NAME, "text-danger")
HATA_MESAJI = (By.CLASS_NAME, "text-danger")
KURUM_ADI_DATA_MESAJI = (By.CSS_SELECTOR, "span[data-testid='institution-error']")


#Test Data

DATA_KURUM_ADI="ENOCTA"
DATA_POZISYON="YAZILIM TEST UZMANI"
DATA_SEKTOR="YAZILIM"
DATA_SEHIR="İstanbul"
DATA_IS_BASLANGIC="01.01.2020" #gg.aa.yyyy
DATA_IS_BITIS="30.04.2020"
DATA_IS_ACIKLAMASI="YAZILIM TESTLERINI OTOMASYONA DOKMEK"
DATA_IS_GIRIS_YILI="2020"
DATA_IS_BASLANGIC_AY="Ocak"
DATA_IS_BITIS_YIL="2023"
DATA_IS_BITIS_AY="Nisan"
EXPECTED_TARIH_ARALIGI="01.01.2020 - Devam Ediyor"
DATA_GECERSIZ_KURUM_ADI="dene"