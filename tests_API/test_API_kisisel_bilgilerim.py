import pytest
import requests
import json
import softest
from tests_API.API_constants import *
from API_get_token import *


class TestAPI_kisisel_bilgilerim(softest.TestCase):

    def test_GET_kisisel_bilgilerim(self):

        end_point = base_url + "/user-profile/my"
        token = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(end_point, headers=headers)

        response_data = response.json()

        user_data = response_data[0]

        if response.status_code == 200:
            print("!! Basarili !! ")

            assert (expected_name == user_data['name'] and
                    expected_surname == user_data['surname'] and
                    expected_mail == user_data['email'] and
                    expected_phoneNumber == user_data['phoneNumber'])
        else:

            print("lütfen kodu kontrol et")
            
    def test_POST_kisisel_bilgilerim(self):

        end_point = base_url + "/user-profile/identity-number"
        token = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        payload={"data":{"name":"Tobeto","surname":"Tobeto","identityNumber":"11111111111","year":"1994"}}

        payload_str = json.dumps(payload)

        response = requests.post(end_point, data = payload_str, headers=headers)
        print(response.text)

        if response.status_code == 200:
            print(" !! Basarili !! ")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")
        