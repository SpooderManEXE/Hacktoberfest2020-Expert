import random
No = random.randint(1, 50)
guess = int(raw_input("Enter an integer from 1 to 50: "))
while No != "guess":
    print
    if guess < No:
        print "guess is low"
        guess = int(raw_input("Enter an integer from 1 to 50: "))
    elif guess > No:
        print "guess is high"
        guess = int(raw_input("Enter an integer from 1 to 50: "))
    else:
        print "Congrats!you guessed the number right!"
        break
    print
