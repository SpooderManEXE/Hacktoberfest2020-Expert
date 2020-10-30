def swap(a,b):
       c=b
       b=a
       a=c
       return a,b
x=int(input("enter"))     
y=int(input("enter 2"))
a,b = swap(x,y)
print("a=",a,"b=",b)
