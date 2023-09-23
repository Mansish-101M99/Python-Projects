import random

var = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){{}}[]:;\"\"\'\'/?,.+-*/"
length_pswd = int(input("Enter the length of the password : "))
pswd = "".join(random.sample(var, length_pswd))
print("Your requested password : ",pswd)