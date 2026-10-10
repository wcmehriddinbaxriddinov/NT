import json

student = {
    "name": "Eshmat",    
    "age": 18,    
    "course": "Python",    
    "score": 85
}

with open("/home/mexriddin/Documents/NT/foundation/3-oy/darslar/7-dars/student.json", "w") as f:
    json.dump(student, f, indent=4)
    
print("Fayl saqlandi")