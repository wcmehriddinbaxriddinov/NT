numbers = [10, 20, 30]

a = int(input("Son: "))
b = int(input("Index: "))

try:
    print(numbers[b] / a)
except ValueError:
    print("Son kiritng")
except IndexError:
    print("Index xato kiritildi")