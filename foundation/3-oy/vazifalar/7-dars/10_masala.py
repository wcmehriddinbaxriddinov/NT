while True:
    ism = input("Ism: ")
    if ism.strip() != "":
        break
    print("Ism bo'sh bo'lmasligi kerak")

while True:
    try:
        yosh = int(input("Yosh: "))
        if yosh > 0:
            break
        print("Yosh 0 dan katta bo'lishi kerak")
    except ValueError:
        print("Butun son kiriting")

while True:
    try:
        oylik = int(input("Oylik: "))
        if oylik > 0:
            break
        print("Oylik 0 dan katta bo'lishi kerak")
    except ValueError:
        print("Butun son kiriting")

xodim = {"ism": ism, "yosh": yosh, "oylik": oylik}

with open("foundation/3-oy/vazifalar/7-dars/xodimlar.txt", "a") as file:
    file.write(f"{xodim['ism']} {xodim['yosh']} {xodim['oylik']}\n")
print("Xodim qo'shildi!")