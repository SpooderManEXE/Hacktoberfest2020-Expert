def TripleDouble(num1,num2):
    list1 = num1.split()
    num = 0;
    for i in range(0,len(list1)):
        if(list1[i]==list1[i+1] and list1[i]==list1[i+2]):
            num = list1[i]
            break;
    list2 = num2.split()
    for i in range(0,len(list2)):
        if(list2[i]==list2[i+2] and list2[i]==num):
            return 1
    return 0
number1 =input()
number2 = input()
a = TripleDouble(number1,number2)
print(a)
