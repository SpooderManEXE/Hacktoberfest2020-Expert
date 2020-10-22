number = [12, 5, 67, 78, 8, 9]
svalue = 78

def find(number, svalue):
	#LOGIC
	for i in range(len(number)):
		if svalue == number[i]:
			return True
	return False

if find(number, svalue):
	print("Found")
else:
	print("Not Found")
