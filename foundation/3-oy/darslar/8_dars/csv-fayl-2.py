import csv

with open("foundation/3-oy/darslar/8_dars/mahsulotlar.csv", "r") as f:
    data = csv.reader(f, delimiter="|")
    mahsulotlar = list(data)
    ustnular = mahsulotlar[0]
    print(ustnular)
    
    count = 0
    for mahsulot in mahsulotlar[1:]:
        for i in range(len(ustnular)):
            print(f"{ustnular[i].title()}: {mahsulot[i]}")
        print("-" * 20)
        count += 1
    
    print(f"Mahsulotlar soni: {count}")
            