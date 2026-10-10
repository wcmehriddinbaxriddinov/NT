while True:
    nomi = input("Nomi: ")
    if nomi != "":
        break
    print("Nomi bo'sh bo'lmasligi kerak")

while True:
    try:
        narxi = float(input("narxi: "))
        if narxi > 0:
            break
        print("Narxi 0 dan katta bo'lishi kerak")
    except ValueError:
        print("Son kiriting")

while True:
    try:
        miqdori = float(input("Miqdori: "))
        if miqdori > 0:
            break
        print("Miqdori 0 dan katta bolishi kerak")
    except ValueError:
        print("Son kiriting")

mahsulot = {
    "nomi": nomi, 
    "narxi": narxi, 
    "miqdori": miqdori
}

with open("foundation/3-oy/vazifalar/7-dars/mahsulotlar.txt", "a") as file:
    file.write(f"{mahsulot['nomi']} {mahsulot['narxi']} {mahsulot['miqdori']}\n")
print("Mahsulot qo'shildi!")
