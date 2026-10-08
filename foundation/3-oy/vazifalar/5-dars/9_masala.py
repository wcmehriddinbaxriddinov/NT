def ortacha(ballar):
    if len(ballar) == 0:
        return "Ballar yo‘q"

    return sum(ballar) / len(ballar)


ballar = input("Ballarni kiriting: ").split()

sonlar = []

for ball in ballar:
    sonlar.append(int(ball))

print(ortacha(sonlar))

assert ortacha([60, 80]) == 70.0
assert ortacha([]) == "Ballar yo‘q"