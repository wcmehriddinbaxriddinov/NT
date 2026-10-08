import requests

url = input("Links: ")

data = requests.get(url=url)
name = url.split("/")[-1]
if data.status_code == 200:
    print(f"{name} yuklandi")
    f = open(name, 'wb')
    f.write(data.content)
else:
    print("Ma'lumot olsihda xatolik")