#tip calculator to split tip between friends
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("what percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip = total_bill *(tip_percentage/100) 
total_bill = total_bill + tip
final= (total_bill /people)

print(f"Each person should pay {round(final, 2)} ")

