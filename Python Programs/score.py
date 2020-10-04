ss = input("Enter Score: ")
score = float(ss)
try:
    if (score>=0.9):
        print("A")
    elif (score>= 0.8):
        print("B")
    elif (score >= 0.7):
        print("C")
    elif (score >= 0.6):
        print("D")
except:
    print("Enter correct Value")
    quit()
