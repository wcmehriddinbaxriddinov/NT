def elementni_ol(royxat, indeks):
    try:
        return royxat[indeks]
    except IndexError:
        return "Bunday indeks yo‘q"

n = int(input("Nechta son kerak: "))
royxat = list(map(int, input().split()[:n]))

indeks = int(input("Nechanchi indeks: "))

print(elementni_ol(royxat, indeks))