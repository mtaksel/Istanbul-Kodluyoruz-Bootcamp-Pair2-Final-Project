from selenium.webdriver.common.by import By

KULLANICI_ISIM_BUTONU="//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p"
PROFIL_BILGILERI_BUTONU="//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"
DENEYIMLERIM_BUTONU="//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[2]"
KURUM_ADI_TEXTBOX="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input" #XPATH
POZISYON_TEXTBOX="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"   #XPATH
SEKTOR_TEXTBOX="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input" 
SEHIR_SECINIZ_DROPDOWN="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select"
IS_BITIS_TEXTBOX="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[1]/div/input"
IS_BITIS_YIL="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select"
IS_BITIS_AY="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select"
IS_BITIS_GUN="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]"
IS_BASLANGIC_TEXTBOX="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input"
IS_BASLANGIC_YIL="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select"
IS_BASLANGIC_AY="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select"
IS_BASLANGIC_GUN="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]"
IS_ACIKLAMASI="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea"
CALISMAYA_DEVAM_EDIYORUM_BUTONU="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/label[2]/input"

KAYDEDILEN_DENEYIM_BASLIKLARI=(By.CLASS_NAME,"grade-details-header")
TUM_DENEYIMLER=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div/div/span[2]") # elementsss 



UYARI_MESAJI=(By.CLASS_NAME,"text-danger") 
KAYDET_BUTONU="//*[@id='__next']/div/main/section/div/div/div[2]/form/button" #XPATH
DENEYIM_EKLENDI_MESAJI="toast-body"

SIL_BUTONU="//*[@id='__next']/div/main/section/div/div/div[2]/div/div[1]/div[2]/div[5]/span[1]"
DENEYIM_SIL_EVET_BUTONU="/html/body/div[4]/div/div/div/div/div/div[2]/button[2]" 
DENEYIM_SIL_HAYIR_BUTONU="/html/body/div[3]/div/div/div/div/div/div[2]/button[1]"
DENEYIM_KALDIRILDI_MESAJI="//*[@id='__next']/div/div[2]/div/div[2]"
# EKLENEN DENEYIMIN WEBELEMENTLERI

EKLENEN_KURUM_ADI="//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[1]/span[2]"
EKLENEN_POZISYON="//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[2]/span[2]"
EKLENEN_SEKTOR="//*[@id='__next']/div/main/section/div/div/div[2]/div/div[1]/div[2]/div[3]/span[2]"
EKLENEN_SEHIR="//*[@id='__next']/div/main/section/div/div/div[2]/div/div[1]/div[2]/div[4]/span[2]"
UC_NOKTA="//*[@id='__next']/div/main/section/div/div/div[2]/div/div[1]/div[2]/div[5]/span[2]"
EKLENEN_IS_ACIKLAMASI="/html/body/div[4]/div/div/div[2]/span"
EKLENEN_TARIH_ARALIGI="//*[@id='__next']/div/main/section/div/div/div[2]/div/div[1]/div[1]/span"

#Hata Mesaj
HATA_MESAJI=(By.CLASS_NAME,"text-danger")  # doldurulmasi zorunlu alan uyarisi
KURUM_ADI_DATA_MESAJI=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span") # kurum adi 5 karakterden az olamaz hata mesajı


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