fname = input("Enter file name: ")
ff=open(fname)

for line in ff:
    line=line.rstrip()
    print(line.upper())
