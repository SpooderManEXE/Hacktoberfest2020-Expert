# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num &1) == 0:   #more efficient after using bitwise AND
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
