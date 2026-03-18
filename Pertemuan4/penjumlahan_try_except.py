""" 3.	Buatlah sebuah program yang meminta dua angka. Jumlahkan kedua angka tersebut dan tampilkan hasilnya.
Tangkap (catch) ValueError jika salah satu nilai input bukan angka, 
lalu tampilkan pesan kesalahan yang friendly. Uji program dengan memasukkan dua angka dan 
kemudian dengan memasukkan beberapa teks """

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

except ValueError:
    print("Input harus berupa angka, bukan teks!")