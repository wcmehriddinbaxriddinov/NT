import json

with open("/home/mexriddin/Documents/NT/foundation/3-oy/darslar/7-dars/telefon.json", "r") as f:
    telefon = json.load(f)
    
    print(telefon)
    print(type(telefon))
    