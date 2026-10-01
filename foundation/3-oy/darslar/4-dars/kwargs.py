def info(**malumotlar):
    print("---------- Ma'lumotlar ----------")
    for key, value in malumotlar.items():
        print(f"{key.title()}: {value}")
    print("-" * 20)

info(ism = "Ali", familiya = "Valiyev", yosh = 20)
info(ism = "Ali", familiya = "Valiyev", yosh = 20, shahar = "Farg'ona")