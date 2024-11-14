from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

# Refined Locators
EGITIM_HAYATIM = (By.XPATH, "//a[contains(@href, 'egitim_hayatim')]/span[text()='Eğitim Hayatım']")

EGITIM_DURUMU_BUTONU = (By.NAME, "egitimDurumu")  
LISANS_SEC = (By.XPATH, "//select[@name='egitimDurumu']/option[text()='Lisans']")

UNIVERSITE = (By.ID, "universityInput")  
UNIVERSITE_ADI = "İTÜ"

UNIVERSITE_ADI_HATALI_UYARI_MESAJI = (By.XPATH, "//input[@id='universityInput']/following-sibling::span[contains(@class, 'error-message')]")
UNISVERSITE_ADI_HATALI = "A"
UNIVERSITE_ADI_HATALI_UYARI_MESAJI_TEXT = "En az 2 karakter girmelisiniz"

BOLUM = (By.ID, "departmentInput")  
BOLUM_ADI = "KİMYA"
BOLUM_ADI_DEVAM = "TEST MÜHENDİSİ"
BOLUM_ADI_HATALI = "B"
BOLUM_ADI_HATALI_UYARI_MESAJI = (By.XPATH, "//input[@id='departmentInput']/following-sibling::span[contains(@class, 'error-message')]")
BOLUM_ADI_HATALI_UYARI_MESAJI_TEXT = "En az 2 karakter girmelisiniz"

BASLAMA_YILI_BUTONU = (By.CLASS_NAME, "start-year-dropdown")  
BASLAMA_YILI_SEC = (By.XPATH, "//div[@class='start-year-dropdown']//div[text()='2023']")  

MEZUNIYET_YILI = (By.ID, "graduationYearInput")  
MEZUNIYET_YILI_SEC = (By.XPATH, "//div[@class='graduation-year-dropdown']//div[text()='2024']")  

UNIVERSITEYE_DEVAM_EDIYORUM_BUTONU = (By.XPATH, "//label[contains(text(), 'Üniversiteye Devam Ediyorum')]/input[@type='checkbox']")

BASARILI_POPUP_MESAJ = (By.CLASS_NAME, "toast-body")  
BASARILI_POPUP_MESAJI_TEXT = "• Eğitim bilgisi eklendi."

KAYDET_BUTONU = (By.XPATH, "//button[text()='Kaydet']")

KAYDI_SIL = (By.XPATH, "//span[contains(text(), 'Kaydı Sil')]")
KAYIT_SILMEYE_EMINMISIN_MESAJI = (By.CLASS_NAME, "alert-message")  
KAYIT_SILMEYE_EMINMISIN_MESAJI_TEXT = "Seçilen eğitimi silmek istediğinize emin misiniz?"
EVET_BUTONU = (By.XPATH, "//button[@class='btn btn-yes my-3' and text()='Evet']")

KAYIT_SILME_BASARILI = (By.CLASS_NAME, "toast-body")
KAYIT_SILME_BASARILI_TEXT = "• Eğitim kaldırıldı."

UYARI_MESAJI = (By.XPATH, "//span[contains(text(), 'Doldurulması zorunlu alan*')]")

PROFIL_BILGILERI_BUTTON = (By.XPATH, "//a[contains(@href, 'profil_bilgileri')]")
KULLANICI_BUTTON = (By.XPATH, "//button[contains(@class, 'user-profile-button')]")

FOTO_CEKME_DOSYASI = r'screenshots\egitim_hayatim\zorunlu_alanlari_doldurma_kontrolu.png'
FOTO_CEKME_DOSYASI2 =r'screenshots\egitim_hayatim\universite_eklendi.png'
FOTO_EKME_DOSYASI3 =r'screenshots\egitim_hayatim\universiteye_devam_ediyor.png'
FOTO_CEKME_DOSYASI_BOLUM_ADI_HATALI = r'screenshots\egitim_hayatim\bolum_adi_hatali.png'
FOTO_CEKME_DOSYASI_UNIVERSITE_ADI_HATALI = r'screenshots\egitim_hayatim\universite_adi_hatali.png'