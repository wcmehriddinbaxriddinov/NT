while True:
    ism = input("Talaba ismini kiriting: ")
    if ism.strip() != "":
        break
    print("Ism bo'sh bo'lmasligi kerak")

while True:
    try:
        yosh = int(input("Talaba yoshini kiriting: "))
        if yosh > 0:
            break
        print("Yosh 0 dan katta bo'lishi kerak")
    except ValueError:
        print("Butun son kiriting")

while True:
    try:
        ball = int(input("Talaba ballini kiriting: "))
        if 0 <= ball <= 100:
            break
        print("Ball 0 dan 100 gacha bo'lishi kerak")
    except ValueError:
        print("Butun son kiriting")

talaba = {
    "ism": ism, 
    "yosh": yosh, 
    "ball": ball
}

with open("foundation/3-oy/vazifalar/7-dars/talaba.txt", "w") as file:
    for qiymat in talaba.values():
        file.write(f"{qiymat}\n")
print("Ma'lumot yozildi!")
