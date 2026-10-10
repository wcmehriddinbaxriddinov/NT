with open("/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/numbers.txt", "r") as file:
    malumot = file.readlines()
    sonlar = list(map(int, malumot))

    
    print(sonlar)
    print(sum(sonlar))
    print(max(sonlar))
    print(min(sonlar))