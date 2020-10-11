#calculate 20 factorials using pascal triangle
factorials = []
def pascal_triangle_fact(n):
    for row in range(0,n+1):
        curr_lst = [1]
        for col in range(1,row+1):
            if(row==col):
                curr_lst.append(1)
            else:
                curr_lst.append(factorials[row-1][col]+factorials[row-1][col-1])
        factorials.append(curr_lst)
pascal_triangle_fact(1000)
print("answer",factorials[1000][12])
