arr=[1,2,0,3,5,0,0,6,0,40,9]
n = len(arr)

def mux(n):
    return n*0
A = list(map(mux,arr)) # a blank array of same size as arr, in o(1), map is microscopically fster than loop, if lambda isn't used
# print(A)

j =0
for i in range(n):
    
    if arr[i] !=0:
        
        A[j] = arr[i]
        j +=1
print(A)