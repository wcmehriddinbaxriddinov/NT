def chek_age(age):
    if 0 < age < 150:
        return age
    raise ValueError ("Xatolik")

print(chek_age(5))