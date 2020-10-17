print("linear search")
si=int(input("\nEnter the size:"))
data=list()
for i in range(0,si):
      n=int(input())
      data.append(n)
cot=0
print("\nEnter the number you want to search:")
val=int(input())
for i in range(0,len(data)):
      if(data[i]==val):
            break;
      else:
            cot=cot+1
print(cot)#linear search result=4
#binary search
print("\nBinary Search")
cot=0
beg=0
end=len(data)
mid=(beg+end)/2
mid=int(mid)
while beg<end and val!=data[mid]:
      if val>data[mid]:
            beg=mid+1
      else:
            end=mid-1
      mid=int((beg+end)/2)
      cot=cot+1
if 14==data[mid]:
      print("\nDATA FOUND")
      print(cot)      
