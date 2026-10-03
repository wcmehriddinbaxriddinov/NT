sonlar = [-5, 3, -2, 8, -1]

manfiy = list(filter(lambda son: son < 0, sonlar))

musbat = list(map(abs, manfiy))

print(musbat)