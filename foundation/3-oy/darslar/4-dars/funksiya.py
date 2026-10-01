# funkisya - 1 maarta kodlarni yozib, undan qayta qayta foydalanish uchun
# parametr - ism
# arguments - "Ali"
# natija - none

def salomlashish(ism: str = ".", familiya = ""):
    print(f"Salom, {ism} {familiya}")
    
salomlashish("Ali", "Valiyev")
salomlashish(555) # qiymat int bo'lsa ham xatolik bermay ishlayveradi
salomlashish()


def daraja(son: int, n: int = 2) -> int:
    return son ** n

print(daraja(5, 3))
print(daraja(5))