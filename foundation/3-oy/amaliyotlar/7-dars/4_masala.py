with open('/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/stundents.txt', 'a') as file:
    student = input("Ismingizni kirting: ")
    file.write(student)
    
print("Saqlandi")