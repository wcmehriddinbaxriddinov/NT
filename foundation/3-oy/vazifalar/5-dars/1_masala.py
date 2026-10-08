def xavfsiz_bolish(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0 ga bo‘lish mumkin emas"

a = int(input("a ga qiymat bering: "))
b = int(input("b ga qiymat bering: "))

print(xavfsiz_bolish(a, b))