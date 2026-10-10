with open("/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/numbers.txt", "r") as f:
    sonlar = f.read()
    print(sonlar.split)
    sonlar = list(map(int, sonlar.split()))
    print(sonlar)