import pytest
import requests
import json
import softest
from API_get_token import *
from API_constants import *


class TestAPIEgitimlerim(softest.TestCase): 
        
    
    def test_GET_kayitli_egitimleri_getir(self):
       
        end_point= base_url+ "/educations"
        token= APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1)

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

    
        response = requests.get(end_point, headers=headers)
        
        response_data = response.json() # JSON yanıtını işle
       
        # İlk öğeyi seç
        user_data = response_data[0] 

        expected_educationStatus= "Lisans"
        expected_university= "İTÜ" 
        expected_department= "TEST MÜHENDİSİ"
        expected_startDate= "2023"
        expected_endDate= None
        
        
        if response.status_code == 200:
            print(" !! Basarili !! ")
            assert( expected_educationStatus == user_data['EducationStatus'] and expected_university == user_data['University'] and
                   expected_department == user_data['Department'] and expected_startDate == user_data['StartDate'] and
                   expected_endDate == user_data['EndDate'])
            
                
        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")


    def test_POST_yeni_egitim_ekler(self):
       
        end_point=base_url+"/educations"
        token= APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1)
       
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        #test data
        payload={"data":{"University":"marmara","Department":"muhendislik","Language":"Türkçe","StartDate":"2020","EducationStatus":"Lisans","EndDate":"2024"}}

        # JSON verisini stringe dönüştür
        payload_str = json.dumps(payload) # Gönderilecek JSON verisi str olmalı cunku Post metodu dtring aliyor
        
        # POST isteği yap
        response = requests.post(end_point, data = payload_str, headers=headers) #benim gonderdigim header json
        print(response.text)
        
        if response.status_code == 200:
            print(" !! Basarili !! ")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")


    def test_DELETE_egitim_siler(self):
        
        end_point=base_url+"/educations/6210"
        token= APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1)

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'

        }
        response = requests.delete(end_point,headers=headers)

        if response.status_code == 200:
            print(" !! Basarili !! ")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")

