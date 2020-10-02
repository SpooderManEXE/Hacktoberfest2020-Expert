# reversing using loop and reverse fxn

arr = [1,2,3,4,5]
l = len(arr)
for i in range(l//2):
    # print(i)
    arr[i], arr[l-i-1] = arr[l-i-1], arr[i]
print(arr)

