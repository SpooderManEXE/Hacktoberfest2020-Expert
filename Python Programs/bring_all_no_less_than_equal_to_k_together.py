arr = [2,1,5,6,7,3,2]
k = 3
# we need to bring (2,1,3) <= 3 together in min swap: swapping 5 <--> 3 #SORTING ISN"T ALLOWeed
n = len(arr)

def swap(subarr,l,loc):
    # l = len(subarr)
    subarr[0],subarr[loc] = subarr[loc],subarr[0]
    return subarr # godd subarr

count =0
subarr=[]

for i in range (n) : 
    
    if arr[i] > k: #bad case call swap
        
        subarr = arr[i:] # subarr of format[bad,.......]
        # print(subarr)
        l = len(subarr)

        for j in range(l):
            
            if subarr[j] <= k: # if some element of sub arr is good, swap good and subarr[0]
                
                loc = j
                subarr = swap(subarr,l,loc)
                count += 1
                break
            
        arr[i:] = subarr # adding good subarr to arr

print(count)    # min no of swaps required
print(arr) #required arr


