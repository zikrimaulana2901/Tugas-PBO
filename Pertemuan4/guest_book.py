""" 2.	Tulis perulangan while yang meminta pengguna untuk memasukkan nama mereka. 
Kumpulkan semua nama yang dimasukkan, lalu tulis nama-nama ini ke dalam file bernama guest_book.txt. 
Pastikan setiap entri muncul di baris baru dalam file. """

names = []

while True:
    nama = input("Masukkan nama (ketik 'done' untuk berhenti): ")
    
    if nama == 'done':
        break
    
    names.append(nama)

with open("guest book.txt", "w") as file:
    for nama in names:
        file.write(nama + "\n")

print("Semua nama yang telah ada isi berhasil disimpan ke dalam file guest_book.txt")