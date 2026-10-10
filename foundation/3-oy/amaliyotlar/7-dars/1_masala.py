ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiritng: ")
yosh = int(input("Yoshingizni kiriting: "))

with open("/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/matn.txt", "w") as file:
    file.writelines(f"Ism: {ism} \nFamiliya: {familiya} \nYosh: {yosh}")

print("Ma'lumot yozildi!")