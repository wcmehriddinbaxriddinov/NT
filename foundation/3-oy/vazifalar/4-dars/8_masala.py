n = int(input())
sonlar = list(map(int, input().split()[:n]))

kublar = list(map(lambda son: son ** 3, sonlar))
print(kublar)
