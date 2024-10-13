from selenium.webdriver.common.by import By

EGITIM_HAYATIM = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]")

EGITIM_DURUMU_BUTONU=(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select")
LISANS_SEC= (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]")

UNIVERSITE = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
UNIVERSITE_ADI = "İTÜ"

UNIVERSITE_ADI_HATALI_UYARI_MESAJI = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span")
UNISVERSITE_ADI_HATALI ="A"
UNIVERSITE_ADI_HATALI_UYARI_MESAJI_TEXT ="En az 2 karakter girmelisiniz"

BOLUM= (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input") 
BOLUM_ADI= "KİMYA"
BOLUM_ADI_DEVAM ="TEST MÜHENDİSİ"
BOLUM_ADI_HATALI ="B"
BOLUM_ADI_HATALI_UYARI_MESAJI = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span")
BOLUM_ADI_HATALI_UYARI_MESAJI_TEXT = "En az 2 karakter girmelisiniz"

BASLAMA_YILI_BUTONU = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div")
BASLAMA_YILI_SEC = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[7]") #XPATH

MEZUNIYET_YILI =  (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input") 
MEZUNIYET_YILI_SEC = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[8]") #XPATH

UNIVERSITEYE_DEVAM_EDIYORUM_BUTONU = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/label[2]/input")

BASARILI_POPUP_MESAJ = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
BASARILI_POPUP_MESAJI_TEXT ="• Eğitim bilgisi eklendi."
                     
KAYDET_BUTONU=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")

KAYDI_SIL=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/span")
KAYIT_SILMEYE_EMINMISIN_MESAJI = (By.XPATH,"//body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//p[@class='alert-message mx-3']")
KAYIT_SILMEYE_EMINMISIN_MESAJI_TEXT = "Seçilen eğitimi silmek istediğinize emin misiniz?"
EVET_BUTONU = (By.XPATH,"//body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//button[@class='btn btn-yes my-3']")
KAYIT_SILME_BASARILI = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
KAYIT_SILME_BASARILI_TEXT = "• Eğitim kaldırıldı."

#UYARI MESAJI
UYARI_MESAJI= (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span")
UYARI_MESAJI_TEXT = "Doldurulması zorunlu alan*"

PROFIL_BIGLILERI_BUTTON =(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
KULLANICI_BUTTON = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")

FOTO_CEKME_DOSYASI = r'screenshots\egitim_hayatim\zorunlu_alanlari_doldurma_kontrolu.png'
FOTO_CEKME_DOSYASI2 =r'screenshots\egitim_hayatim\universite_eklendi.png'
FOTO_EKME_DOSYASI3 =r'screenshots\egitim_hayatim\universiteye_devam_ediyor.png'
FOTO_CEKME_DOSYASI_BOLUM_ADI_HATALI = r'screenshots\egitim_hayatim\bolum_adi_hatali.png'
FOTO_CEKME_DOSYASI_UNIVERSITE_ADI_HATALI = r'screenshots\egitim_hayatim\universite_adi_hatali.png'