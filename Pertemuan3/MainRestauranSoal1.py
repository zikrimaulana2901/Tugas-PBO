from RestauranSoal1 import Restaurant

restaurant = Restaurant("ZhyYxx Resto", "Seblak Jutek rasa Emosi")

print(f"Halooo Restaurantku bernama {restaurant.restaurant_name}.")
print(f"Menyediakan menu yaitu {restaurant.jenis_menu}\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nJumlah pelanggan yang dilayani: {restaurant.number_served}")

restaurant.set_number_served(25)
print(f"Jumlah pelanggan setelah diubah: {restaurant.number_served}")

restaurant.increment_number_served(10)
print(f"Jumlah pelanggan setelah ditambah hari ini: {restaurant.number_served}")