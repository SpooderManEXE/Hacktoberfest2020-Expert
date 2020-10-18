class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge<0:
            self.initialAge=0
            print("Age is not valid, setting age to 0.")
        else:
            self.initialAge=initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge<13:
            print("You are young.")
        elif self.initialAge>=13 and self.initialAge<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge+=1

t = int(input())
for i in range(0, t):
    age = int(input("Enter your age: "))         
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
