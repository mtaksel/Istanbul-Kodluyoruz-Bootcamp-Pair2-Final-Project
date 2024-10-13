import requests
import json
from API_constants import *
import softest

from tests_API.API_get_token import *

class TestForeignLanguage(softest.TestCase):

    def test_control_add_language(self):
      token_language = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1_mac)

      headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_language}'
        }  
      
      new_language_data = {"data": {"Language": "3", "Proficiency": "Temel Seviye ( A1 , A2)"}}
         
      data_str = json.dumps(new_language_data)

      response = requests.post(url_language, data = data_str,  headers = headers)

      if response.status_code == 200:
        print("Authentication API sorgusunda geçerli bilgi isteği sonucunda 200 durum kodu görüldü.")
    
      else:
        print("Yeni veri oluşturulurken bir hata oluştu:", response.text)  



    def test_control_added_language(self):
        token_language = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1_mac)
        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_language}'
        }

        response = requests.get(url_language, headers = headers)

        if response.status_code == 200:
            response_data = response.json()

            print("Authentication API sorgusunda geçerli bilgi isteği sonucunda 200 durum kodu görüldü.", response_data)

        elif response.status_code == 401:
            print("Lütfen token güncelleyiniz!!", response.status_code)
        
        elif response.status_code == 404:
            print("!! NotFoundError !! ")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!", response.status_code)

    
    def test_existing_language(self):
       token_language = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1_mac)
       headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_language}'
        }  
      
       new_language_data = {"data": {"Language": "3", "Proficiency": "Temel Seviye ( A1 , A2)"}} 
       data_str = json.dumps(new_language_data)
       response = requests.post(url_language, data = data_str,  headers = headers)

       if response.status_code == 200:
        print("Var olan bir veri eklemeye çalışma sonucunda 200 durum kodu görüldü.")
    
       else:
        print("Beklenmeyen bir hata oluştu:", response.text)

    def test_control_delete_language(self):
        token_language = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1_mac)
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_language}'
        }

        response = requests.delete(url_delete_language, headers = headers)

        if response.status_code == 200:
            print("Body başarıyla silindi.")
        else:
            print("Body silinirken bir hata oluştu:", response.text)

# TestForeignLanguage.control_added_language()

