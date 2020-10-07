ijk = input().split()
a = int(ijk[0])
b = int(ijk[1])
k = int(ijk[2])
li = [i for i in range(a,b+1)]
lid = list(map(str,li))
lis = []
count = 0
for i in range(len(lid)):
    lis.append(int(''.join(list(reversed(lid[i])))))
    if(abs(int(lid[i])-lis[i])%k==0):
        count += 1
print(count)