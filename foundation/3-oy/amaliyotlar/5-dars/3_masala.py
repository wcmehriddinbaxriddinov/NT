names = ["Ali", "Vali", "Hasan", "Husan"]
index = int(input("Indexni kiritng: "))
if index < len(names):
    print(f"Indexda joylashgan ma'lumot: {names[index]}")
else:
    raise IndexError("No'malum index")