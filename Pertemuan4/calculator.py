""" 5.	Buatlah program kalkulator sederhana di Python beserta unit testing-nya
menggunakan unittest """ 


class Calculator:

    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return a / b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa modulus dengan nol")
        return a % b

    def pangkat(self, a, b):
        return a ** b

    def pembagian_bulat(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa pembagian bulat dengan nol")
        return a // b


if __name__ == "__main__":
    calcu = Calculator()

    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        print("Penjumlahan:", calcu.tambah(a, b))
        print("Pengurangan:", calcu.kurang(a, b))
        print("Perkalian:", calcu.kali(a, b))
        print("Pembagian:", calcu.bagi(a, b))
        print("Modulus:", calcu.modulus(a, b))
        print("Pangkat:", calcu.pangkat(a, b))
        print("Pembagian Bulat:", calcu.pembagian_bulat(a, b))

    except ValueError as e:
        print("Error:", e)