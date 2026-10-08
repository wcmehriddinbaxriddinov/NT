def ballni_tekshir(ball):
    if 0 > ball or ball > 100:
        raise ValueError ("0 dan katta yoki 100 dan kichik son kiriting!")
    
    return ball

ball = int(input("Ballingizni kiriitng: "))

print(ballni_tekshir(ball))