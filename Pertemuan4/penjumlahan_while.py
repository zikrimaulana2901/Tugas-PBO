""" 4.	Bungkus kode program dari Latihan dan Tugas (4-a) nomor 2 
dalam perulangan while agar pengguna dapat terus memasukkan angka, 
meskipun mereka membuat kesalahan dan memasukkan teks sebagai pengganti angka. """

while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)

    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar!")

    repeat = input("Coba lagi? (ketik 'done' untuk berhenti): ")

    if repeat == 'done':
        break