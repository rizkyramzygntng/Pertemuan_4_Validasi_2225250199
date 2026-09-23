try:
    nilai_ujian = float(input("Masukkan nilai ujian: "))
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    kehadiran = float(input("Masukkan persentase kehadiran: "))

    if not (0 <= nilai_ujian <= 100):
        print("Nilai ujian harus berada pada rentang 0-100.")
    elif not (0 <= nilai_tugas <= 100):
        print("Nilai tugas harus berada pada rentang 0-100.")
    elif not (0 <= kehadiran <= 100):
        print("Persentase kehadiran harus berada pada rentang 0-100.")
    else:
        nilai_akhir = (0.6 * nilai_ujian) + (0.4 * nilai_tugas)

        if kehadiran < 80:
            print(f"Nilai akhir: {nilai_akhir:.2f}")
            print("Predikat: -")
            print("Status: Tidak memenuhi syarat kehadiran")
        else:
            if nilai_akhir >= 85:
                predikat = "A"
                status = "Lulus"
            elif nilai_akhir >= 70:
                predikat = "B"
                status = "Lulus"
            elif nilai_akhir >= 60:
                predikat = "C"
                status = "Lulus"
            elif nilai_akhir >= 50:
                predikat = "D"
                status = "Belum lulus"
            else:
                predikat = "E"
                status = "Belum lulus"

            print(f"Nilai akhir: {nilai_akhir:.2f}")
            print(f"Predikat: {predikat}")
            print(f"Status: {status}")

except ValueError:
    print("Input harus berupa angka.")