n = int(input())
sonlar = list(map(int, input().split()[:n]))

kublari = list(map(lambda son: son ** 3, sonlar))
print(kublari)
