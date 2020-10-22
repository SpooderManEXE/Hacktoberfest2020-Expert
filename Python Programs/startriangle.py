#star triangle generator script

a = 1
b = int(input('Input Number : '))
c = b

while(a<=b):
    print(' '*c,'*'*a)
    a+=2
    c-=1