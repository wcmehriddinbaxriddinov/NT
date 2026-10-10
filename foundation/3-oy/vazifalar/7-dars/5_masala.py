while True:
    try:
        n = int(input("Nechta mahsulot malumotini saqlamoqchisiz: "))
        if n > 0:
            break
        else:
            print("0 dan katta raqam kiritng")
    except ValueError:
        print("Butun son kiriting")
    
mahsulotlar = []

for mahsulot in range(n):
    print(f"{mahsulot + 1} - talaba:")
    
    while True:
        nomi = input("Nomi: ")
        if nomi != "":
            break
        else:
            print("Nomi bo'sh bolmasligi kerak")
        
    while True:
        try:
            narxi = float(input("Yosh: "))
            if narxi > 0:
                break
            else:
                print("Narxi 0 dan katta bolishi kerak")
        except ValueError:
            print("Butun son kiriting")
    
    while True:
        try:
            miqdori = float(input("Ball: "))
            if miqdori > 0:
                break
            else:
                print("Miqdori 0 dan katta bolishi kerak")
        except ValueError:
            print("Son kiritng")
    
    mahsulot = {
        "nomi": nomi,
        "narxi": narxi,
        "miqdori": miqdori
    }
    
    mahsulotlar.append(mahsulot)
    
    with open("foundation/3-oy/vazifalar/7-dars/mahsulotlar.txt", "w") as file:
        for mahsulot in mahsulotlar:
            file.write(f"{mahsulot['nomi']} {mahsulot['narxi']} {mahsulot['miqdori']}\n")
    print("Malumot yozildi")
    
    