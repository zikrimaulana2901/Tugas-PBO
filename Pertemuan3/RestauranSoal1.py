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