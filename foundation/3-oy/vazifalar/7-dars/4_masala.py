while True:
    try:
        n = int(input("Nechta talaba ma'lumotini saqlamoqchisiz: "))
        if n > 0:
            break
        else:
            print("0 dan katta raqam kiritng")
    except ValueError:
        print("Butun son kiriting")
    
talabalar = []

for talaba in range(n):
    print(f"{talaba + 1} - talaba:")
    
    while True:
        ism = input("Ism: ")
        if ism.strip() != "":
            break
        else:
            print("Ism bo'sh bolmasligi kerak")
        
    while True:
        try:
            yosh = int(input("Yosh: "))
            if yosh > 0:
                break
            else:
                print("Yosh 0 dan katta bolishi kerak")
        except ValueError:
            print("Butun son kiriting")
    
    while True:
        try:
            ball = int(input("Ball: "))
            if 0 <= ball <= 100:
                break
            else:
                print("Ball 0 dan katta bolishi kerak")
        except ValueError:
            print("Butun son kiritng")
    
    talaba = {
        "ism": ism,
        "yosh": yosh,
        "ball": ball
    }
    
    talabalar.append(talaba)
    
    with open("foundation/3-oy/vazifalar/7-dars/talabalar.txt", "w") as file:
        for talaba in talabalar:
            file.write(f"{talaba['ism']} {talaba['yosh']} {talaba['ball']}\n")
    print("Malumot yozildi")
    
    