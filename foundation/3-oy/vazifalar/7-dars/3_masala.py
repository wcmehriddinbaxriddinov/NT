while True:
    marka = input("Markasini kiriting: ")
    if marka != "":
        break
    else:
        print("Marka nomi bosh bo'lmasligi kerak")

while True:
    try:
        yil = int(input("Ishlab chiqarilgan yilini kiritng: "))
        if yil <= 2026:
            break
        else:
            print("Ishlab chiqarilgan yil 2026 katta bolishi mumkin emas")
    except ValueError:
        print("Yil sonda bo'lish kerak")

while True:
    try:
        narx = float(input("Narxini kiritng: "))
        if narx > 0:
            break
        else:
            print("Narx 0 dan kichik bolishi mumkin emas")
    except ValueError:
        print("Narxga son kiritili lozim")

Avtomobil = {
    "marka": marka,
    "yil": yil,
    "narx": narx
}

with open("foundation/3-oy/vazifalar/7-dars/avtomobil.txt", "w") as file:
    for qiymat in Avtomobil.values():
        file.write(f"{qiymat}\n")
    print("Ma'lumot yozildi")
    
            