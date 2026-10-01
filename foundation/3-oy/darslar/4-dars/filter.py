sonlar = [5, 3, 9, 20, 13]

juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar)) # filtr shartga mos ma'lumotlarni olib qoladi

print(type(juft_sonlar))
print(juft_sonlar)