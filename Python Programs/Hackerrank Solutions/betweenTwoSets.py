def getTotalX(a, b):
    aray=[]
    possible = []
    aray = [i for i in range(a[-1],b[0]+1)]
    index = 0
    possible = aray.copy()
    for i in a:
        for j in range(len(aray)):
            if (aray[j]%i != 0):
                if aray[j] in possible:
                    index = possible.index(aray[j])
                    possible.pop(index)
    for j in b:
        for i in range(len(aray)):
            if (j%aray[i] != 0):
                if aray[i] in possible:
                    index = possible.index(aray[i])
                    possible.pop(index)
    return len(possible)
