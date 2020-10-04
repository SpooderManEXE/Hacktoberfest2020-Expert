# Bubble Sort Algorithm
# Sorts values in lowest to largest order

values = [] # initialized empty list
# List length input
listLen = int(input("Enter the length of the list: "))

for i in range(0, listLen):
	# List values input
	valInput = int(input("Enter the values: "))
	values.append(valInput)

n = len(values) # takes length of values

# Sorting Process
for i in range(0, n-1):
	for j in range(0, n-1):
		# Swapping the value 
		if values[j] > values[j+1]:
			temp = values[j+1]
			values[j+1] = values[j]
			values[j] = temp

# print's the sorted value
for i in range(0, n):
	print(values[i], " ", end="")
