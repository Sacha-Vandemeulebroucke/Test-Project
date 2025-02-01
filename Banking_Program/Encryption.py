import string
import random

chars = string.ascii_letters + string.digits +string.punctuation + " "

chars= list(chars)
keys = chars.copy()
random.shuffle(keys)

print(chars)
print(keys)

sen_to_encrypt = str(input("Enter a sentence "))
encrypted=""
decrypted=""


for char in sen_to_encrypt:
    encr = chars.index(char)
    encr_2 = keys[encr]
    encrypted += encr_2

print(encrypted)

for char in encrypted:
    decr = keys.index(char)
    decr2 = chars[decr]
    decrypted += decr2

print(decrypted)