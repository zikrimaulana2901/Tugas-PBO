# SOAL 1
""" 1.	Buat kelas bernama Restaurant. untuk Restaurant Metode __init__() harus menyimpan dua atribut: nama restoran (restaurant_name)
dan jenis masakan (cuisine_type). Buatlah metode bernama describe_restaurant() yang mencetak kedua informasi ini,
dan metode bernama open_restaurant() yang mencetak pesan yang menunjukkan bahwa restoran tersebut dibuka. 
Buat instance bernama restaurant dari kelas Anda. Cetak kedua atribut tersebut secara terpisah, lalu panggil kedua metode tersebut.."""

class Restaurant:
    def __init__(self, restaurant_name, jenis_menu):
        self.restaurant_name = restaurant_name
        self.jenis_menu = jenis_menu

    def describe_restaurant(self):
        print(f"Nama Restaurant: {self.restaurant_name}")
        print(f"jenis Menu: {self.jenis_menu}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} DIBUKAAAAA SEKARANG !!!!!!")

restaurant = Restaurant("ZhyYxx Resto", "Seblak Jutek rasa Emosi")

print(f"Halooo Reastaurantku bernama {restaurant.restaurant_name}.")
print(f"Menyediakan menu yaitu {restaurant.jenis_menu}\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
