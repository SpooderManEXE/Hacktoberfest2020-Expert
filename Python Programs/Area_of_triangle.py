# Python Program to find the area of triangle using Heron's Formula.
#enter all the sides of triangle from user.
 a = float(input('Enter first side: '))
 b = float(input('Enter second side: '))
 c = float(input('Enter third side: '))
# now, using formula , calculate the semi-perimeter
s = (a + b + c) / 2
# and calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#now, print the output.
print('The area of the triangle is %0.2f' %area)
#end of code.
