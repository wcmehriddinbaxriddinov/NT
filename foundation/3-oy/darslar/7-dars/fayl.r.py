with open("/home/mexriddin/Documents/NT/foundation/3-oy/darslar/7-dars/matn.txt") as f:
    # matn = f.read()  # hamma ma'lumot str ko'rinishida olinadi
    
    # matnlar = f.readlines()
    
    qatorlar = f.readlines() # har bir qatorni list ko'riinishida oladi
    
    for qator in qatorlar:
        print(qator)
    print("-----------------------------")

    # print(type(matn))
    # print(matn)
    # print("-----------------------------")
    
    # print(type(matnlar))
    # print(matnlar)