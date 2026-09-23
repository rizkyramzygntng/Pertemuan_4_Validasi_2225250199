try:
    benar = int(input("Masukkan jumlah jawaban benar: "))

    if benar < 0 or benar > 20:
        print("Jumlah jawaban benar tidak valid.")
    else:
        persentase = (benar / 20) * 100

        if persentase >= 75:
            print("Tuntas")
        else:
            print("Belum tuntas")

except ValueError:
    print("Input harus berupa bilangan bulat.")