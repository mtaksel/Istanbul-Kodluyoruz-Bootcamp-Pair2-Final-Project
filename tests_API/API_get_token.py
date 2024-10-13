import requests
import json
from datetime import datetime, timedelta
from API_constants import *

class APIAutoToken():
    @staticmethod
    def get_saved_token(file_path):
        try:
            with open(file_path, "r") as file:
                data = file.read().strip().split(",")
                if len(data) == 2:  # Kaydettiğimiz token ın doğruluğunu uzunluğundan doğruluyoruz.
                    token = data[0]
                    expiration = datetime.fromisoformat(data[1])
                    return token, expiration
                else:
                    return None, None
        except FileNotFoundError:
            return None, None

    @staticmethod
    def save_token(token, expiration, file_path):
        with open(file_path, "w") as file:
            file.write(f"{token},{expiration.isoformat()}")

    @staticmethod
    def is_token_expired(expiration):
        return datetime.now() >= expiration

    @staticmethod
    def API_get_token(url, payload, file_path):
        # Token ın tarihinin geçerliliğini kontrol et.
        token, expiration = APIAutoToken.get_saved_token(file_path)
        if token and expiration and not APIAutoToken.is_token_expired(expiration):
            return token

        # JSON verisini stringe dönüştür
        payload_str = json.dumps(payload) 

        # POST isteği yap
        response = requests.post(url, data=payload_str, headers={'Content-Type': 'application/json'})
        
        # Çağrının doğruluğunu kontrol et.
        if response.status_code == 200:
            # Response.json dan "jwt" yi çek.
            jwt_token = response.json().get("jwt")
            expiration_time = datetime.now() + timedelta(hours=24)
            if jwt_token:
                APIAutoToken.save_token(jwt_token, expiration_time, file_path)  # Token ı geçerlilik süresi ile sakla.
                return jwt_token
            else:
                print("JWT token response.json içerisinde bulunamadı.")
        else:
            print(f"Giriş hatası kodu: {response.status_code}")


# # Çağrı denemesi
# jwt_token = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_1, TOKEN_FİLE_PATH_1)
# if jwt_token:
#     print("JWT token:", jwt_token)

# jwt_token = APIAutoToken.API_get_token(TOBETO_AUTH_URL, TOBETO_PAYLOAD_2, TOKEN_FİLE_PATH_2)
# if jwt_token:
#     print("JWT token:", jwt_token)

