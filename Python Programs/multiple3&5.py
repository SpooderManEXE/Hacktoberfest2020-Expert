#multiple of 3 and 5 script

for x in range(1,101):
    if(x%3==0 and x%5==0):
        print('it is the multiple of both')
    elif(x%3==0):
        print('multiple of 3????')
    elif(x%5==0):
        print('which multiple is this one')
    else:
        print(x)