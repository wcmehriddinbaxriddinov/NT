with open("/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/stundents.txt", "r") as f: 
    students = f.readlines()
    
    for student in students:
        print(student)

print("Ish bajarildi")