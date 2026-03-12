# SOAL 2
""" 2.	Dari soal nomor 1, buatlah 3 instance berbeda dari kelas tersebut, dan panggil describe_restaurant() untuk setiap instance """

class Restaurant:
    def __init__(self, restaurant_name, jenis_menu):
        self.restaurant_name = restaurant_name
        self.jenis_menu = jenis_menu

    def describe_restaurant(self):
        print(f"Nama Restaurant: {self.restaurant_name}")
        print(f"jenis Makanan: {self.jenis_menu}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} BUKAAAAA SEKARANG !!!!!!")

restaurant1 = Restaurant("ZhyYxx Resto", "Seblak Jutek rasa Emosi")
restaurant2 = Restaurant("Teras Teduh Resto", "Mie Akhirat")
restaurant3 = Restaurant("Anak Senja Resto", "Tahu Gejrot Emosi")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
