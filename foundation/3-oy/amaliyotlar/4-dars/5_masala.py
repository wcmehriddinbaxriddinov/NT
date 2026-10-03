sonlar = [2,3,4,5,6,7,8,9,11]

def isTub(son):
    for i in range(2, son):
        if son % i == 0:
            return False
        else:
            return True

tublar = list(filter(isTub, sonlar))

print(tublar)
        