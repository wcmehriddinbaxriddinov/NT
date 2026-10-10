# file = open("matn.txt", "w")
# file.write("Salom")

# with
with open("/home/mexriddin/Documents/NT/foundation/3-oy/darslar/7-dars/matn.txt", "a") as file:
    file.write("Salom") # bu oddiy yozish funksiyasi
    file.writelines(
        ["Fayl ochildi" "Faylga saqlandi"]) # bu list orqali yozish

print("Ma'lumot yozildi!")