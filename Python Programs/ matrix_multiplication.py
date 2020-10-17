x = [[3,4],
     [1,2]]

y = [[6,9],
     [5,8]]

xy = [[0,0],
      [0,0]]

n=2
for i in range(n):
    for j in range(n):
        xy[i][j] = x[i][j] * y[i][j]

print(xy)