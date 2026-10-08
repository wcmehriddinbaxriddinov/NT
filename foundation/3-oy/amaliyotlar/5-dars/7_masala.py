def check_pasword(pasword):
    if len(pasword) < 8:
        raise ValueError("Parol kamida 8 ta belgi bo'lsin")
    return True

pasword = input("parol kiriting: ")

try:
    print(check_pasword(pasword))
except ValueError as e:
    print(e)