import requests

data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json")

data = data.json()

while True:
    kod = input("Valyutda kodini kiritng: ").strip().upper()

    natija = False

    for val in data:
        if val['Ccy'] == kod:
            value = float(val['Rate'])
            print(f"1 {kod} = {value} so\'m")
            natija = True
            break
        
    if natija:
        print("Muvafaqiyatli bajarildi!")
    else:
        print("Valyuta mavud emas yoki valyuta kodi xato!")
    
    tanlov = input("Quyidagilardan birini tanlang:\n 1 - qayta urinish\n 0 - to\'xtatish\n tanlang: ")
    
    if tanlov == "0":
        print("Dastur to\'xtatildi.")
        break