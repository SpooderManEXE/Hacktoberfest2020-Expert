arr = [1, 34, 3, 98, 9, 76, 45, 4]
l = len(arr)
digits =[]

# # Uncomment and use either of the 2 digitconverter

# def digitconverter(num):
#     # digit = []
#     while num !=0:
#         digits.append(num%10)
#         num = num//10

# def digitconverter(num):
#     number = str(num)
#     for i in range(len(number)):
#         digits.append(int(number[i]))


    

for i in range(l):
    if arr[i] >=10:
        digitconverter(arr[i])
    else:
        digits.append(arr[i])
# print(digits)
digits.sort()
digits = digits[::-1] #descending order sort
# print(digits) # array of max no. possible
n = "".join(map(str,digits)) # converting every digit to str

print(n) # required max no. possible



