# Generating random password using list comprehension

import random
import string

pass_len = int(input("Enter the length of the password : "))

charValues  = string.ascii_letters + string.digits + string.punctuation

#using list comprehension
password = "".join([random.choice(charValues) for i in range(pass_len)])



print("Your random password is : ", password)