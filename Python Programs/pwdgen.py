import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345467890!@#$%^&*()-=+[]"
n = int( input("Enter your password length: ") )

pwd = ''

for i in range(n):
    c = random.choice( chars )
    pwd = pwd + c  

print("Your new strong level password is: ", pwd)
