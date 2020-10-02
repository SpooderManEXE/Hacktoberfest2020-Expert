while True:
    try:
        num=int(input("Input your number: "))
        print("Your number is {}".format(num))
        break
    except:
        print("Please insert number!")