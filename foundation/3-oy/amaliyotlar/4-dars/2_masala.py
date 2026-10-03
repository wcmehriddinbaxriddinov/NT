sonlar = [-6, 5, -9, -5, 4, -3]

def custom_abs(son):
    return son if son > 0 else -son

musbat = list(map(custom_abs, sonlar))

print(musbat)