""" 1.	Tulis program yang meminta pengguna untuk memasukkan nama mereka. 
Ketika mereka merespons, tulis nama mereka ke dalam file bernama guest.txt. """

nama = input("Masukkan nama Anda: ")

with open("guest.txt", "w") as file:
    file.write(nama)

print("Nama anda berhasil disimpan ke dalam file guest.txt")