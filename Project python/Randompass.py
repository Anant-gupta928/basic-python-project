import random
import string

pass_len = int(input("press the lenght of password that you suggest:"))
value = string.ascii_letters + string.digits + string.punctuation 
password = ""
for i in range(pass_len):
 password+=random.choice(value)
print("your random password is:",password)
