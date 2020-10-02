#upside down star triangle generator script
#input odd number if you want a perfect triangle

a = 0
c = int(input('Input Number : '))

while(c>=0):
    print(' '*a,'*'*c)
    a+=1
    c-=2