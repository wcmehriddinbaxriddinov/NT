def talaba_info(**malumotlar):
	for kalit, qiymat in malumotlar.items():
		print(f"{kalit}: {qiymat}")


talaba_info(Ism="Aziz", Kurs=2, Shahar="Samarqand")
