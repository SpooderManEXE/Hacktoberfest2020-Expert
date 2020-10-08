def reverseVowels(s):
    word=list(s)
    vowels={'a','e','o','u','i','A','E','O','U','I'}
    left=0
    right=len(word)-1
    while(left<right):
        if(word[left] not in vowels):
            left+=1
        elif(word[right] not in vowels):
            right-=1
        else:
            word[left],word[right]=word[right],word[left]
            left,right=left+1,right-1  
    s=""
    return(s.join(word))
