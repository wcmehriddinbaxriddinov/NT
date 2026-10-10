import csv

with open("foundation/3-oy/darslar/8_dars/mahsulotlar.csv", "r") as f:
    mahsulotlar = csv.reader(f, delimiter="|")
    
    for mahsulot in mahsulotlar:
        print(mahsulot)