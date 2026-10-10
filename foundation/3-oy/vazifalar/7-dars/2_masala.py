while True:
    nomi = input("Mahsulot nomini kiriting: ")
    if nomi != "":
        break
    else:
        print("Nomi bo'sh bo'lmasligi kerak")

while True:
    try:
        narxi = int(input("Mahsulot narxini kiriting: "))
        if narxi > 0:
            break
        else:
            print("Narx 0 dan kichik bo'lishi mumkin emas")
    except ValueError:
        print("Narx butun sonda. Butun son kiritng")

while True:
    try:
        miqdori = float(input("Mahsulot miqdorini kiritng: "))
        if miqdori > 0:
            break
        else:
            print("Mahsulot miqdori 0 bol'ishi mumkin emas")
    except ValueError:
        print("Son kiritign")

mahsulot = {
    "nomi": nomi,
    "narxi": narxi,
    "miqdori": miqdori
}

with open("foundation/3-oy/vazifalar/7-dars/mahsulot.txt", "w") as file:
    for qiymat in mahsulot.values():
        file.write(f"{qiymat}\n")
print("Ma'lumot yozildi!")