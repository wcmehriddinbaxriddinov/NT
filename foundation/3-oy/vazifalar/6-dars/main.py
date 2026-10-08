from match_tools import kvadrat, juftmi

while True:
    try:
        number = int(input("Son kiriting: "))
        break
    except ValueError:
        print("Butun son kiriting!")
    
print(f"{number} ning kvadrati = {kvadrat(number)}")

if juftmi(number):
    print(f"{number} juft son")
else:
    print(f"{number} toq son")
    
assert kvadrat(number) == number **2
assert juftmi(number) == (number % 2 == 0)

print("Muvafaqiyatli ishladi!")