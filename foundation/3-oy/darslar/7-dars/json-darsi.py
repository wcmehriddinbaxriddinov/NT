import json

telefon = {
    "nom": "A33",
    "ram": "6GB",
    "rang": "qora"
}

with open("/home/mexriddin/Documents/NT/foundation/3-oy/darslar/7-dars/telefon.json", "w") as f:
    json.dump(telefon, f, indent=4)
    
t = json.dumps(telefon, indent=4)
print(type(t))
print(t)