prices = [9000, 15000, 22000, 14000, 30000]

tozalash = list(filter(lambda son: son >= 10000, prices))
qoshish = list(map(lambda son: son-2000, tozalash))

print(f"Natija: {qoshish}")
