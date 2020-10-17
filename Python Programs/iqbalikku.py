largest = None
smallest = None
while True:
   num =input("Entera number: ")
   if num == "done": 
        break
   try:
    num=int(num)
    if largest is None:
     largest=num
    elif largest<num:
     largest=num
     
    if smallest is None:
     smallest=num
    elif smallest>num:
     smallest=num
   except:
     c=1
     continue
if c==1:
 print('invalid input')
print('Maximum is', largest)
print('Minimum is', smallest)
