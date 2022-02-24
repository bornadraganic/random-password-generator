import random
import string


characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter your password length here: ")) 

for i in range(length):
    password = "".join(random.sample(characters, length))



print(password)
