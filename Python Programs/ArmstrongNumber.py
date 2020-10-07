no = int(input())
sum = 0
temp = no
while temp > 0:
    digit = temp%10
    sum += digit**3
    temp //= 10
if no == sum:
    print(no, 'is armstrong number')
else:
    print('try again')