str1=input("Enter the string")
for i in range(len(str1)):
	if str1[i] not in str1[:i]:
		print(str1[i],"->",str1.count(str1[i]))
