while True:
    try:
        n = int(input("Nechta xodim ma'lumotini saqlamoqchisiz: "))
        if n > 0:
            break
        print("0 dan katta son kiriting")
    except ValueError:
        print("Butun son kiriting")

xodimlar = []

for i in range(n):
    print(f"{i + 1}-xodim:")

    while True:
        ism = input("Ism: ")
        if ism.strip() != "":
            break
        print("Ism bo'sh bo'lmasligi kerak")

    while True:
        try:
            yosh = int(input("Yoshi: "))
            if yosh > 0:
                break
            print("Yosh 0 dan katta bo'lishi kerak")
        except ValueError:
            print("Butun son kiriting")

    while True:
        try:
            oylik = float(input("Oylik: "))
            if oylik > 0:
                break
            print("Oylik 0 dan katta bo'lishi kerak")
        except ValueError:
            print("Son kiriting")

    xodim = {"ism": ism, "yosh": yosh, "oylik": oylik}
    xodimlar.append(xodim)


with open("foundation/3-oy/vazifalar/7-dars/xodimlar.txt", "a") as file:
    for xodim in xodimlar:
        file.write(f"{xodim['ism']} {xodim['yosh']} {xodim['oylik']}\n")
print("Ma'lumot yozildi")