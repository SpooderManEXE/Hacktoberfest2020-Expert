# Sum of natural numbers up to num

num = int(input())
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   for i in range(num):
      sum += i
   print("The sum is", sum)
