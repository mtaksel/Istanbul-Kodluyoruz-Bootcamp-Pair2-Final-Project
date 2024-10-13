import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.giris_constants import *


@pytest.mark.usefixtures("setup")
class Giris(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def username_bul_ve_gönder(self, data):
        user_name= self.wait_element_visibility(USERNAME_LOCATOR)
        user_name.send_keys(data)

    def password_bul_ve_gönder(self, data):
        password = self.wait_element_visibility(PASSWORD_LOCATOR)
        password.send_keys(data)

    def giris_yap_butonuna_tikla(self):
        self.wait_element_clickable(GIRISYAPBUTTON_LOCATOR).click()    

    def toast_mesaji_bul_text_döndür(self):
        toast_message_basarılı = self.wait_element_presence(TOASTMESSAGE_LOCATOR)
        return toast_message_basarılı.text
    
    def hata_satirlarini_bul_ve_döndür(self):
        error_line_mail = self.wait_element_presence(BOS_ERROR_LINE_MAIL)
        error_line_password = self.wait_element_presence(BOS_ERROR_LINE_PASSWORD)
        return error_line_mail.text, error_line_password.text

    def ana_giris(self):
        user_name= self.wait_element_visibility(USERNAME_LOCATOR)
        user_name.send_keys(GIRISMAIL)
        password = self.wait_element_visibility(PASSWORD_LOCATOR)
        password.send_keys(GIRISSIFRE)
        self.wait_element_clickable(GIRISYAPBUTTON_LOCATOR).click()
        
    # def gecerli_giris(self):
    #     self.ana_giris()
    #     toast_message_basarılı = self.wait_element_presence(TOASTMESSAGE_LOCATOR)
    #     #assert toast_message_basarılı.text ==  BASARILI_POPUP_TEXT
    #     return toast_message_basarılı.text
    #     #self.soft_assert(self.assertEqual, toast_message_basarılı.text, BASARILI_POPUP_TEXT, "Basarili pop up goruntulenemedi.")

    # def gecersiz_giris(self):
    #     user_name= self.wait_element_visibility(USERNAME_LOCATOR)
    #     user_name.send_keys(GECERSIZMAIL)
    #     password = self.wait_element_visibility(PASSWORD_LOCATOR)
    #     password.send_keys(GECERSIZSIFRE)
    #     self.wait_element_visibility(GIRISYAPBUTTON_LOCATOR).click()
    #     toast_message_gercersiz = self.wait_element_presence(TOASTMESSAGE_LOCATOR)
    #     return toast_message_gercersiz.text
   
    # def bos_giris(self):
    #     user_name= self.wait_element_visibility(USERNAME_LOCATOR)
    #     user_name.send_keys("")
    #     password = self.wait_element_visibility(PASSWORD_LOCATOR)
    #     password.send_keys("")
    #     self.wait_element_visibility(GIRISYAPBUTTON_LOCATOR).click()
    #     error_line_mail = self.wait_element_presence(BOS_ERROR_LINE_MAIL)
    #     error_line_password = self.wait_element_presence(BOS_ERROR_LINE_PASSWORD)
    #     return error_line_mail.text, error_line_password.text



        
       
        