# Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
arr_new=[]
for i in range(len(arr)):
    arr_new.append(0)
nos =[]
for i in range (len(arr)):
    x = arr[i]
    if x != -1:
        nos.append(x)
nos.sort()
nos_x =0
for i in range(len(arr)):
    
    if i == nos[nos_x]:
        
        nos_x +=1
        # print(nos_x)
        arr_new[i]= i
        # print(arr_new)
    elif i != nos[nos_x]:
        
        arr_new[i] = -1
        # print(arr_new)

print(arr_new)
