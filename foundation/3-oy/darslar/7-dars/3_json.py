import json

with open("foundation/3-oy/darslar/7-dars/student.json", "+") as f:
    student = json.load(f)
    
    for key in student:
        print(f"{key}: {student[key]}")
        
    student["score"] += 10
    
    print(student)

    json.dump(student, f, indent=4)