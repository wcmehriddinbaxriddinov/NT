def otgan_ballar(ballar):
    natija = []

    for ball in ballar:
        if ball >= 60:
            natija.append(ball)

    return natija


ballar = input("Ballarni kiriting: ").split()

sonlar = []

for ball in ballar:
    sonlar.append(int(ball))

print(otgan_ballar(sonlar))

assert otgan_ballar([59, 60, 75, 40]) == [60, 75]
assert otgan_ballar([60]) == [60]
assert otgan_ballar([]) == []