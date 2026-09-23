# Pertemuan 04 — Seleksi Multi-Kondisi dan Validasi Input

**Nama:** Muhammad Rizky Ramzy Ramadhan

**NIM:** 2225250199

**Kelas:** 3E

**Program Studi:** Pendidikan Matematika

**Universitas:** Universitas Sultan Ageng Tirtayasa

## Tujuan

Pada pertemuan ini saya mempelajari penggunaan `if-elif-else` untuk membuat seleksi multi-kondisi dan melakukan validasi input berdasarkan tipe, rentang, dan kondisi yang ditentukan.

## Struktur Project

```text
pertemuan-04-validasi-2225250075/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_predikat_nilai.py
│   ├── 02_kategori_bilangan.py
│   ├── 03_validasi_rentang.py
│   ├── 04_validasi_tipe.py
│   └── 05_klasifikasi_segitiga_sudut.py
└── praktik/
    └── validasi_klasifikasi_nilai.py
```

## Cara Menjalankan

Jalankan program melalui terminal menggunakan Python 3.

Contoh:

```bash
python3 latihan/01_predikat_nilai.py
```

Untuk Praktik 1:

```bash
python3 praktik/validasi_klasifikasi_nilai.py
```

## Tabel Keputusan

### 1. Predikat Nilai

| Kondisi                | Predikat |
| ---------------------- | -------- |
| nilai >= 85            | A        |
| nilai >= 70            | B        |
| nilai >= 60            | C        |
| nilai >= 50            | D        |
| selain kondisi di atas | E        |

### 2. Kategori Bilangan

| Kondisi                 | Kategori       |
| ----------------------- | -------------- |
| bilangan < 0            | Negatif        |
| bilangan == 0           | Nol            |
| bilangan > 0 dan genap  | Positif genap  |
| bilangan > 0 dan ganjil | Positif ganjil |

### 3. Validasi Rentang Sudut

| Kondisi                      | Hasil           |
| ---------------------------- | --------------- |
| sudut <= 0 atau sudut >= 180 | Tidak valid     |
| sudut < 90                   | Sudut lancip    |
| sudut == 90                  | Sudut siku-siku |
| sudut > 90                   | Sudut tumpul    |

### 4. Validasi Tipe

| Kondisi                    | Hasil              |
| -------------------------- | ------------------ |
| input bukan bilangan bulat | Input tidak valid  |
| jumlah benar < 0 atau > 20 | Jumlah tidak valid |
| persentase >= 75%          | Tuntas             |
| persentase < 75%           | Belum tuntas       |

### 5. Klasifikasi Segitiga Berdasarkan Sudut

| Kondisi               | Hasil              |
| --------------------- | ------------------ |
| salah satu sudut <= 0 | Tidak valid        |
| jumlah sudut != 180°  | Tidak valid        |
| sudut terbesar > 90°  | Segitiga tumpul    |
| sudut terbesar == 90° | Segitiga siku-siku |
| sudut terbesar < 90°  | Segitiga lancip    |

### 6. Praktik 1 — Validasi dan Klasifikasi Nilai

Nilai akhir dihitung dengan:

```text
nilai akhir = (0.6 × nilai ujian) + (0.4 × nilai tugas)
```

| Kondisi                                   | Hasil                           |
| ----------------------------------------- | ------------------------------- |
| Nilai ujian/tugas/kehadiran di luar 0–100 | Input ditolak                   |
| Input bukan angka                         | Input ditolak                   |
| Kehadiran < 80%                           | Tidak memenuhi syarat kehadiran |
| Nilai akhir >= 85                         | A — Lulus                       |
| Nilai akhir >= 70                         | B — Lulus                       |
| Nilai akhir >= 60                         | C — Lulus                       |
| Nilai akhir >= 50                         | D — Belum lulus                 |
| Nilai akhir < 50                          | E — Belum lulus                 |

## Hasil Pengujian

### Latihan 1 — Predikat Nilai

| Input | Output |
| ----: | :----- |
|    92 | A      |
|    85 | A      |
|  84.9 | B      |
|    70 | B      |
|    60 | C      |
|    50 | D      |
|  49.9 | E      |

### Latihan 2 — Kategori Bilangan

| Input | Output         |
| ----: | :------------- |
|    -7 | Negatif        |
|     0 | Nol            |
|     8 | Positif genap  |
|    13 | Positif ganjil |

### Latihan 3 — Validasi Rentang

| Input | Output            |
| ----: | :---------------- |
|    45 | Sudut lancip      |
|    90 | Sudut siku-siku   |
|   135 | Sudut tumpul      |
|     0 | Sudut tidak valid |
|   180 | Sudut tidak valid |
|   -30 | Sudut tidak valid |

### Latihan 4 — Validasi Tipe

|     Input | Output            |
| --------: | :---------------- |
|        15 | Tuntas            |
|        14 | Belum tuntas      |
|        20 | Tuntas            |
|         0 | Belum tuntas      |
|        21 | Tidak valid       |
| dua belas | Input tidak valid |

### Latihan 5 — Klasifikasi Segitiga

| Input       | Output             |
| ----------- | ------------------ |
| 60, 60, 60  | Segitiga lancip    |
| 90, 45, 45  | Segitiga siku-siku |
| 120, 30, 30 | Segitiga tumpul    |
| 100, 50, 40 | Segitiga tumpul    |
| 0, 90, 90   | Tidak valid        |

### Praktik 1

| Ujian | Tugas | Kehadiran | Hasil                           |
| ----: | ----: | --------: | ------------------------------- |
|    90 |    80 |        95 | 86.00 — A — Lulus               |
|    75 |    70 |        85 | 73.00 — B — Lulus               |
|    60 |    60 |        80 | 60.00 — C — Lulus               |
|    55 |    50 |        90 | 53.00 — D — Belum lulus         |
|    40 |    30 |       100 | 36.00 — E — Belum lulus         |
|    90 |    90 |        75 | Tidak memenuhi syarat kehadiran |
|   105 |    80 |        90 | Nilai ujian tidak valid         |
|    80 |    -5 |        90 | Nilai tugas tidak valid         |
|    80 |    80 |       abc | Input harus berupa angka        |

## Refleksi

Dari latihan ini saya memahami bahwa `if-elif-else` digunakan untuk menentukan hasil berdasarkan beberapa kondisi. Saya juga belajar bahwa input perlu divalidasi terlebih dahulu, terutama untuk memastikan tipe dan rentang nilainya sesuai.

Pada Praktik 1, saya belajar menggabungkan validasi input dengan perhitungan nilai akhir dan klasifikasi predikat. Urutan kondisi juga penting karena kehadiran harus diperiksa sebelum menentukan predikat dan status kelulusan.
