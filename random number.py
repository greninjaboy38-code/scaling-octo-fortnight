import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

password_list = random.sample(characters, length)
password = "".join(password_list)

print("Generated password:", password)
