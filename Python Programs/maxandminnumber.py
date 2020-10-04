largest = -1
smallest = None
while True:
    n = input("Enter a number: ")
    if n == "done" : break
    try:
        num = float(n)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest=num
    elif num < smallest:
        smallest=num

    if num > largest:
        largest=num


print("Maximum is", largest)
print("Minimum is", smallest)
