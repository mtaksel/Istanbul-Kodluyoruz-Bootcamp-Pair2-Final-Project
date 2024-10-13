import requests
import json
import softest
from API_constants import *
from API_get_token import APIAutoToken

class TestAPI(softest.TestCase):
    def test_valid_login(self):
        expected_email = "tobeto.0002@gmail.com"
        # Gerçek API endpoint URL'si
        url = "https://api.tobeto.com/api/auth/local"
  
        payload = {"identifier":"tobeto.0002@gmail.com",   
        "password":"TestTobeto1234"}

        # JSON verisini stringe dönüştür
        payload_str = json.dumps(payload) # Gönderilecek JSON verisi str olmalı cunku Post metodu dtring aliyor

        # POST isteği yap
        response = requests.post(url, data = payload_str, headers={'Content-Type': 'application/json'}) #benim gonderdigim header json

        # API'den gelen yanıtı kontrol et
        if response.status_code == 200:
            
             response_data = response.json() # JSON yanıtını işle
             actual_username = response_data['user']['email']
             assert actual_username == expected_email   
            
             print("Authentication API basariyla caglrildi.")  #izin/kimlik(login en temel izindir)      
        else:
         print("Authentication API isteği başarisiz oldu:", response.status_code)
         
    def test_invalid_login(self): 
        expected_username = "tobeto.0002@gmail.com"
        
        url = "https://api.tobeto.com/api/auth/local"

        payload = {"identifier":"wrong@gmail.com",
                    "password":"TestTobeto1234"}

       
        payload_str = json.dumps(payload) 

        # POST isteği yap #header ı karsiya sorgunun json oldugunu belirtmek için yazıyoruz
        response = requests.post(url, data = payload_str, headers={'Content-Type': 'application/json'}) #benim gonderdigim header json

        # API'den gelen yanıtı kontrol et
        if response.status_code == 400:
            
             response_data = response.json() # JSON yanıtını işle
             actual_username = response_data['error']['status']
             assert actual_username != expected_username   
            
             print("Authentication API sorgusunda invalid username istegi sonucunda 400 status code goruldu.")   
        else:
         print("Invalid username API isteği sonucu başarisiz dondu:", response.status_code)
    
    def test_user_info_isValid(self):
        expected_username = "Test"
        expected_surname = "Tobeto"
        expected_phoneNumber = "+905050000000"
    
        url = "https://api.tobeto.com/api/user-profile/my"
        token = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_2, TOKEN_FİLE_PATH_2_mac)
    
    
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers)
        print(response.text)
        print("--------------------------------------------")
        
       
        
    # API'den gelen yanıtı kontrol et
        if response.status_code == 200:
            
             # Yanıtın Content-Type'ını kontrol et
            # ????assert 'application/json' in response.headers['Content-Type'], "API JSON yanıtı döndürmelidir"

            response_data = response.json() # JSON yanıtını işle
        
        # İlk öğeyi seç
            user_data = response_data[0]
        
            actual_name = user_data['name']
            actual_surname = user_data['surname']
            actual_phoneNum = user_data['phoneNumber']
        
            assert (actual_name == expected_username and 
                actual_surname == expected_surname and 
                actual_phoneNum == expected_phoneNumber), \
               f"Expected: {expected_username}, {expected_surname}, {expected_phoneNumber}. \
               Actual: {actual_name}, {actual_surname}, {actual_phoneNum}"

            print("Authentication API sorgusunda geçerli bilgi isteği sonucunda 200 durum kodu görüldü.")
        else:
            print("Geçersiz kullanici adi API isteği başarisiz oldu:", response.status_code)
            
            
            
   

# TestAPI.test_valid_login()

# TestAPI.test_invalid_login()

# TestAPI.test_user_info_isValid()
