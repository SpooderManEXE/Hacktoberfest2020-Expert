def weeklyPay(hours, wage):
    if hours > 40:
        return 40 * wage + (hours - 40) * wage * 1.5
    else:
        return hours * wage
 
def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("This is an invalid value. Try again. ")
 
hours = getFloat("How many hours did you work? ")
wage = getFloat("What was your hourly rate? ")
 
pay = weeklyPay(hours, wage)
 
print(f"Total pay: ${pay:.2f} ")
