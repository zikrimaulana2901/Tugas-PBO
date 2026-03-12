from UserSoal2 import User

user = User("Zikri", "Maulana", "Laki-Laki", "Pekanbaru, 20 Mei 2002", "zikrimaulana@email.com", "0877-2893-2367")

user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()


print(f"Jumlah login attempts: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts setelah reset: {user.login_attempts}")