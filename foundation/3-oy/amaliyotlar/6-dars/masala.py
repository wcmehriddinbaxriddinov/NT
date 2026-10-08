import requests
from pprint import pprint

data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json")

data = data.json()

tanlov = int(input("Tanlov: "))

match tanlov:
    case 1:
        summa = int(input("Pulni kiriting sumda: "))

        for val in data:
            if val['Ccy'] == "USD":
                value = float(val['Rate'])
                print(f"{summa} so'm = {round(summa / value, 3)} USD")
                break

    case 2:
        summa = int(input("Pulni kiriting USD da: "))

        for val in data:
            if val['Ccy'] == "USD":
                value = float(val['Rate'])
                print(f"{summa} USD = {round(summa * value, 3)} UZS")
                break
    
    case 3:
            summa = int(input("Pulni kiriting sumda: "))
    
            for val in data:
                if val['Ccy'] == "RUB":
                    value = float(val['Rate'])
                    print(f"{summa} so'm = {round(summa / value, 3)} RUB")
                    break
    
    case 4:
            summa = int(input("Pulni kiriting sumda: "))
    
            for val in data:
                if val['Ccy'] == "RUB":
                    value = float(val['Rate'])
                    print(f"{summa} rub = {round(summa * value, 3)} UZS")
                    break