def ijobiy_yigindi(*sonlar):
	yigindi = 0
	for son in sonlar:
		if son > 0:
			yigindi += son
	return yigindi


n = int(input())
sonlar = list(map(int, input().split()[:n]))
print(ijobiy_yigindi(*sonlar))