#using fermats theorem we can able to handle 10^9 factorial not more than that
p = (10**9)+7
def mult(a,b,p):
    return (a%p * b%p)%p

def multiply(a,b,c,p):
    return (a%p * b%p * c%p)%p
def exp(a,b,p):
    if(b==1):
        return a%p
    if(b==0):
        return 1
    temp = exp(a,b//2,p)
    ans = mult(temp,temp,p)
    if(b%2==0):
        return ans
    else:
        return mult(ans,a,p)

factorials = [1,1]
inverses = [1,1]
for j in range(2,10000):
    fact = mult(j,factorials[j-1],p)
    factorials.append(fact)
    inv = exp(fact,p-2,p)
    inverses.append(inv)

print(multiply(factorials[23],inverses[12],inverses[11],p))
