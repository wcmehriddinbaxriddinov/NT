students = []

for student in range(5):
    student = input("Ismingizni kiriting: ")
    students.append(student)

with open("/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/stundents.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Ma'lumotlar yozildi")