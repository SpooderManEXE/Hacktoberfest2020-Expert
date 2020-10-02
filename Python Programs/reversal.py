arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
i=0
while i != n//2:
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    i+=1

print(arr)