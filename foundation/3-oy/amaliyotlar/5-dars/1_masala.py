a = int(input("a: "))
b = int(input("b: "))

try:
    print(a / b)
except ZeroDivisionError:
    print("Sonni 0 ga bo'lish mumkin emas")