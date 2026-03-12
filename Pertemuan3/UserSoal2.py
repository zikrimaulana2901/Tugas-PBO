""" 2.	Berdasarkan program dari Latihan/ Tugas sebelumnya (class User), 
lanjutkan dengan menambahkan atribut bernama login_attempts ke kelas User. 
Tulis metode bernama increment_login_attempts() yang menambah nilai login_attempts sebesar 1. 
Tulis metode lain bernama reset_login_attempts() yang mengatur ulang nilai login_attempts menjadi 0. 
Buat instance dari kelas User dan panggil increment_login_attempts() beberapa kali. 
Cetak nilai login_attempts untuk memastikan nilainya telah ditambah dengan benar, lalu panggil reset_login_attempts(). 
Cetak login_attempts lagi untuk memastikan nilainya telah diatur ulang menjadi 0 """

class User:
    def __init__(self, first_name, last_name, jenis_kelamin, TTL, email, nomor_telfon):
        self.first_name = first_name
        self.last_name = last_name
        self.jenis_kelamin = jenis_kelamin
        self.TTL = TTL
        self.email = email
        self.nomor_telfon = nomor_telfon
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full Name     : {self.first_name} {self.last_name}")
        print(f"Jenis Kelamin : {self.jenis_kelamin}")
        print(f"TTL           : {self.TTL}")
        print(f"Email         : {self.email}")
        print(f"Nomor Telepon : {self.nomor_telfon}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Salam Kenal ;) .\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0