a = input("a = ")
b = input("b = ")

try:
    a = int(a)
    b = int(b)
    print(a + b)
    print(a / b)
except ZeroDivisionError:
    print("Sonni 0 ga bo'lish mumkin emas")
except TypeError:
    print("Ma'lumot turlari mos emas")
except ValueError:
    print("Notog'ri qiymat kiritldi")
except:
    print("Nimadir xato ketdi")