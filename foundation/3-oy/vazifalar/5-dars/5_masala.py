def bonus_qosh(ball):
    return ball + 5


ball = int(input("Ball kiriting: "))

natija = bonus_qosh(ball)
print(natija)

assert bonus_qosh(70) == 75
assert bonus_qosh(0) == 5

print("Barcha testlar muvaffaqiyatli o'tdi!")