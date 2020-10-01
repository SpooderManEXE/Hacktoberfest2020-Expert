prime=101

def RabinKarp(text,pattern):
    n=len(text)
    m=len(pattern)
    texthash=Hash(text[0:len(pattern)])
    patternhash=Hash(pattern)
    
    for i in range(n-m+1):
        if texthash==patternhash:
            if check(text[i:i+m],pattern):
                return True
        if i<n-m:
            texthash=AgainHash(text,i,i+m,texthash,m)
    return False
def AgainHash(text,old,new,oldhash,m):
    newhash=oldhash-ord(text[old])
    newhash/=prime
    newhash+=ord(text[new])*pow(prime,m-1)
    return newhash
    
def Hash(text):
    hash1=0
    for i in range(len(text)):
        hash1+=ord(text[i])*pow(prime,i)
    return hash1
def check(text,pattern):
    if len(text)!=len(pattern):
        return False
    i,j=0,0
    for i,j in zip(text,pattern):
        if i!=j:
            return False
    return True
    
print(RabinKarp("abcdefz","bcd"))
