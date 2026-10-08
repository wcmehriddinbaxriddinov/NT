import random

chegara = [1, 100]

urunishlar=0

while True:
    taxmin = random.randint(*chegara)
    print(f"Siz o'ylagan son {taxmin} ga tengmi? ({chegara})")
    natija = input("(>, <, =): ")
    if natija == "=":
        print(f"🥳🥳 Men bu sonni topdim. {taxmin}")
        print("shuncha urunishda topdi",urunishlar)
        break
    elif natija == "<":
        print("☹️ Qaytadan urinib ko'raman.")
        chegara[1] = taxmin-1
        urunishlar+=1
    else:
        print("☹️ Qaytadan urinib ko'raman.")
        chegara[0] = taxmin+1
        urunishlar+=1

    if chegara[0] >= chegara[1]:
        print("😠 Yolg'on javoblar berildi!")
        break
