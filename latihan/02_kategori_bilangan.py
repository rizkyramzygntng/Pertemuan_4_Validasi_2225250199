bilangan = int(input("Masukkan bilangan: "))

if bilangan < 0:
    kategori = "Negatif"
elif bilangan == 0:
    kategori = "Nol"
elif bilangan % 2 == 0:
    kategori = "Positif genap"
else:
    kategori = "Positif ganjil"

print("Kategori:", kategori)
