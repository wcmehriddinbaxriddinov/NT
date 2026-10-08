def chegirmali_narxlar(narx_matnlari, chegara):
    if chegara < 0:
        raise ValueError("Chegara manfiy bo‘lishi mumkin emas")

    natija = []

    for narx in narx_matnlari:
        try:
            narx = int(narx)
        except:
            continue

        if narx >= chegara:
            natija.append(narx - 2000)

    return natija


narxlar = input("Narxlarni kiriting: ").split()
chegara = int(input("Chegarani kiriting: "))

print(chegirmali_narxlar(narxlar, chegara))


assert chegirmali_narxlar(["9000", "10000", "15000", "x"], 10000) == [8000, 13000]
assert chegirmali_narxlar([], 10000) == []
assert chegirmali_narxlar(["5000", "7000"], 6000) == [5000]