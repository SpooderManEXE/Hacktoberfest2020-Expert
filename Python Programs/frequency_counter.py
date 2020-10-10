L = [11,22,66,22,11,44,55,66,88,77,22,11,44,22,33,77,55,44]
print('The given list is: ')
print(L)
D = {}
for item in L:
if item not in D:
D[item] = L.count(item)
print('Frequency of different items is:')
print(D)
