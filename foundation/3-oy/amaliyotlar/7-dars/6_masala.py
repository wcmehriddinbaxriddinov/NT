with open('/home/mexriddin/Documents/NT/foundation/3-oy/amaliyotlar/7-dars/user.txt', 'a') as file:
    ism = input("Ismingizni kirting: ")
    shahar = input("Yashash joyingizni kiritng: ")
    file.writelines(ism + '\n')
    file.writelines(shahar)
    
print("Saqlandi")