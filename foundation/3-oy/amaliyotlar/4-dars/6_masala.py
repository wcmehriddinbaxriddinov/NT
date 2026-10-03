sonlar = [1,2,3,4,5,6,7,8,9,10]

juft = list(filter(lambda son: son % 2 == 0, sonlar))
kubi = list(map(lambda son: son * son, sonlar))
yigindi = list(sum(sonlar))

print(juft)
print(kubi)
print(yigindi)