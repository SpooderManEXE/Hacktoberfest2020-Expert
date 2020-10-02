arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
s = set()
for i in range (len(arr)):
    s.add(arr[i])

# print(s)
#fixing arr
for i in range(len(arr)): #by no means i can be "-1"
    if i in s:
        arr[i] = i
    else:
        arr[i] = -1

print(arr)