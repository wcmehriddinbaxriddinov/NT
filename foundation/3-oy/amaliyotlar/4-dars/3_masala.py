"""
sonlar = [-6, 5, -9, -5, 4, -3, 7, 8, 12, 34]

def isMusbat(son):
    if son > 0:
        return True
    else:
        return False

# natija = list(filter(lambda son: son > 0, sonlar))

natija = list(filter(isMusbat, sonlar))

print(natija)
"""

"""
text = "1 2 3 4 5 6 7 8 9 10"

sonlar = list(map(int, text.split()))

print(f"Ma'lumot turi: {type(sonlar)}")
"""

son = '25'
son = int(son)

