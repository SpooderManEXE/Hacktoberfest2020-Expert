num = int(input("Print sum of odd numbers till : "))
sum = 0;

for i in range(1, num + 1):

    #Check for odd or not.
    if(not (i % 2) == 0):
        sum += i;

print("\nSum of odd numbers is",sum)
