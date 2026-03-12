""" 1.	Berdasarkan program dari Latihan/ Tugas sebelumnya (class Restaurant), 
lanjutkan dengan Jumlah Pelanggan yang dilayani ! Dengan cara tambahkan atribut 
bernama number_served dengan nilai default 0. Buat instance bernama restaurant dari kelas ini. 
Cetak jumlah pelanggan yang telah dilayani oleh restoran, lalu ubah nilai ini dan cetak lagi. 
Tambahkan metode bernama set_number_served() yang memungkinkan dapat mengatur jumlah pelanggan yang telah dilayani. 
Panggil metode ini dengan angka baru dan cetak nilainya lagi. 
Tambahkan metode bernama increment_number_served() yang memungkinkan dapat menambah jumlah pelanggan yang telah dilayani. 
Panggil metode ini dengan angka apa pun yang dapat mewakili berapa banyak pelanggan yang dilayani dalam, misalnya dalam satu hari"""

class Restaurant:
    def __init__(self, restaurant_name, jenis_menu):
        self.restaurant_name = restaurant_name
        self.jenis_menu = jenis_menu
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama Restaurant: {self.restaurant_name}")
        print(f"Jenis Menu: {self.jenis_menu}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} DIBUKAAAAA SEKARANG !!!!!!")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers