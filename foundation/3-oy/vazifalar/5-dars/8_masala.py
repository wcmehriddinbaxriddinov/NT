def narxlarni_ol(narx_matnlari):
    natija = []

    for narx in narx_matnlari:
        try:
            narx = int(narx)
            natija.append(narx)
        except ValueError:
            print("Noto‘g‘ri narx:", narx)

    return natija


narxlar = input("Narxlarni kiriting: ").split()

print(narxlarni_ol(narxlar))