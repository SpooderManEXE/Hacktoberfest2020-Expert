def removeDuplicates(nums):
    i,j=0,1
    while(i<j and j<len(nums)):
        if(nums[j]!=nums[i]):
            i+=1
            j+=1
        else:
            del nums[j]
    return len(nums)
