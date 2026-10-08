import requests
from pprint import pprint

data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json")

print(data)
if data.status_code == 200:
    valyutalar = data.json()
    pprint(valyutalar)
    
    for valyuta in valyutalar:
        print(valyuta['CcyNm_UZ'], valyuta['Rate'], "so'm")