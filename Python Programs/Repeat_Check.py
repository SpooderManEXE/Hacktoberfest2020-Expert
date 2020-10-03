def repfree(s):
    size=len(s)
    c1=False
    repeated =[]
    for i in range(size):
        k = i+1
        for j in range(k,size):
            if s[i] == s[j] and s[i] not in repeated:
                c1=True
                break
    if c1==True:
        return True
    else:
        return False

a=repfree("23ab")
