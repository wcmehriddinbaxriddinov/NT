while True:
    try:
        n = int(input("Nechta avtomobil ma'lumotini saqlamoqchisiz: "))
        if n > 0:
            break
        print("0 dan katta son kiriting")
    except ValueError:
        print("Butun son kiriting")

avtomobillar = []

for i in range(n):
    print(f"{i + 1}-avtomobil:")

    while True:
        marka = input("Marka: ")
        if marka.strip() != "":
            break
        print("Marka bo'sh bo'lmasligi kerak")

    while True:
        try:
            yili = int(input("Yili: "))
            if 1900 <= yili <= 2026:
                break
            print("Yili 1900 dan 2026 gacha bo'lishi kerak")
        except ValueError:
            print("Butun son kiriting")

    while True:
        try:
            narxi = float(input("Narxi: "))
            if narxi >= 0:
                break
            print("Narxi 0 dan kichik bo'lmasligi kerak")
        except ValueError:
            print("Son kiriting")

    avtomobil = {"marka": marka, "yili": yili, "narxi": narxi}
    avtomobillar.append(avtomobil)

with open("foundation/3-oy/vazifalar/7-dars/avtomobillar.txt", "a") as file:
    for avtomobil in avtomobillar:
        file.write(f"{avtomobil['marka']} {avtomobil['yili']} {avtomobil['narxi']}\n")
print("Ma'lumot yozildi")