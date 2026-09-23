a = float(input("Masukkan sudut pertama: "))
b = float(input("Masukkan sudut kedua: "))
c = float(input("Masukkan sudut ketiga: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sudut tidak valid.")
elif abs(a + b + c - 180) > 1e-9:
    print("Jumlah sudut harus 180 derajat.")
else:
    sudut_terbesar = max(a, b, c)

    if sudut_terbesar > 90:
        print("Segitiga tumpul.")
    elif sudut_terbesar == 90:
        print("Segitiga siku-siku.")
    else:
        print("Segitiga lancip.")