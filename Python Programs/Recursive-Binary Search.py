#Function to perform Binary Search recursively
def Recursive_BSearch(arr,low,high,key):
    if (low==high):
        if arr[low]==key:
            return low
        else:
            return 0
    else:
        mid=int((low+high)/2)
        if key==arr[mid]:
            return mid
        elif key<arr[mid]:
            return Recursive_BSearch(arr,low,mid-1,key)
        elif key>arr[mid]:
            return Recursive_BSearch(arr,mid+1,high,key)
        else:
            return 0


#Program to find an element from an array using Recursive Binary Search
arr=[]
n=int(input("Enter the size of the array : "))
print("Enter the array elements in ascending order :")
for i in range(n):
    item=int(input("Enter element : "))
    arr.append(item)
    
low=0
high=(n-1)
key=int(input("Enter the element to be searched for : "))

pos=Recursive_BSearch(arr,low,high,key)

if (pos):
    print("Element found at position ",(pos+1))
else:
    print("Element not found !!")

    

            
            
        
        


