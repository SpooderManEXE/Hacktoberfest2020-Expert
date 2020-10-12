# Python 3 program to find closest 
# tidy number smaller than the 
# given number 

def tidyNum(str, len): 

	for i in range(len-2, -1, -1): 
	
		# check whether string 
		# violates tidy property 
		if (str[i] > str[i+1]): 
		
			# if string violates tidy 
			# property, then decrease the 
			# value stored at that index by 1 
			# and replace all the value 
			# stored right to that index by 9 
			str[i] -= 1
			for j in range(i+1, len): 
				str[j] = 9
		
	return str

# Driver code 
str = [1,1,3,3,3,4,4,5,5,3,8] 
len = len(str) 
	
# num will store closest tidy number 
num = tidyNum(str, len) 

for i in range(0,len): 
	print(str[i], end = "") 

# This code is contributed by 
# Smitha Dinesh Semwal 
