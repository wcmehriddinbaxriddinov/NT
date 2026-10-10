import csv 

qatorlar = [
    ["id", "familiya", "yosh"],
    ["1", "Ali", "Valiyev", '20'],
    ["2", "Eshmat", "Qobilov", "24"]
]

with open("foundation/3-oy/darslar/8_dars/talabalar.csv", "w") as f:
    writer = csv.writer(f)
    
    # for qator in qatorlar:
    #    writer.writerow(qator)
    
    writer.writerows(qatorlar)