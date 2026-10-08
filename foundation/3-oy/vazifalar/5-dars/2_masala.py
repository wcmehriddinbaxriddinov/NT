def ballni_ol(matn):
    try:
        return int(matn)
    except ValueError:
        return "Ball son bo‘lishi kerak"

matn = input("Ballni yozma ravishda kiritng: ")

print(ballni_ol(matn))
