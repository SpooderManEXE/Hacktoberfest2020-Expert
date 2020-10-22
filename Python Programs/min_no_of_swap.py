def minSwap(arr, n, k) : 
      
    # Find count of elements 
    # which are less than  
    # equals to k 
    count = 0
    for i in range(0, n) : 
        if (arr[i] <= k) : 
            count = count + 1
      
    # Find unwanted elements  
    # in current window of  
    # size 'count' 
    bad = 0
    for i in range(0, count) : 
        if (arr[i] > k) : 
            bad = bad + 1
      
    # Initialize answer with  
    # 'bad' value of current 
    # window 
    ans = bad 
    j = count 
    for i in range(0, n) : 
          
        if(j == n) : 
            break
              
        # Decrement count of 
        # previous window 
        if (arr[i] > k) : 
            bad = bad - 1
          
        # Increment count of  
        # current window 
        if (arr[j] > k) : 
            bad = bad + 1
          
        # Update ans if count  
        # of 'bad' is less in 
        # current window 
        ans = min(ans, bad) 
  
        j = j + 1
  
    return ans 
  
# Driver code 
arr = [2, 1, 5, 6, 3] 
n = len(arr) 
k = 3
print (minSwap(arr, n, k)) 