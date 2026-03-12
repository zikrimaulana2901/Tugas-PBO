# SOAL 3
""" 3.	Buatlah kelas bernama User. Buat dua atribut bernama first_name dan last_name, 
lalu buat beberapa atribut lain yang biasanya disimpan dalam profil User. 
Buat metode bernama describe_user() yang mencetak ringkasan informasi pengguna. 
Buat metode lain bernama greet_user() yang mencetak salam pribadi kepada user. 
Buatlah beberapa instance yang mewakili user yang berbeda, dan panggil kedua metode tersebut untuk setiap user"""

class User:
    def __init__(self, first_name, last_name, jenis_kelamin, TTL, email, nomor_telfon):
        self.first_name = first_name
        self.last_name = last_name
        self.jenis_kelamin = jenis_kelamin
        self.TTL = TTL
        self.email = email
        self.nomor_telfon = nomor_telfon

    def describe_user(self):
        print(f"Full Name     : {self.first_name} {self.last_name}")
        print(f"Jenis Kelamin : {self.jenis_kelamin}")
        print(f"TTL           : {self.TTL}")
        print(f"Email         : {self.email}")
        print(f"Nomor Telepon : {self.nomor_telfon}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Salam Kenal ;) .\n")

user1 = User("Zikri", "Maulana", "Laki-Laki", "Pekanbaru, 20 Mei 2002", "zikrimaulana@email.com", "0877-2893-2367")
user2 = User("Andi", "Saputra", "Laki-Laki", "Dumai, 22 Agustus 2000", "andisaputra@email.com", "0825-8923-2378")
user3 = User("Siti", "Rahma", "Perempuan", "Tasimalaya, 15 September 1998", "sitirahma@email.com", "0897-4567-4572")
user4 = User("Budi", "Pekerti", "Laki-Laki", "Jember, 25 Desember 2003", "budipekerti@email.com", "0895-7456-4567")
user5 = User("Aliando", "Simanjuntak","Laki-Laki", "Jakarta, 29 april 1995", "aliandosimanjuntak@email.com", "0879-4757-3456")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()

user5.describe_user()
user5.greet_user()

