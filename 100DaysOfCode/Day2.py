print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage_bill =  int(input("What percentage tip would you like to give? 5, 10, or 15? "))

while percentage_bill != 5 and percentage_bill != 10 and percentage_bill != 15:
    percentage_bill =  int(input("You have to choose between 10, 12, or 15 percentage "))

people = int(input("How many people to split the bill? "))

total_amount = total_bill + (total_bill * (percentage_bill/100))
bill_per_person = (total_amount / people)

print("Each person should pay: ${:.2f}".format(round(bill_per_person,2)))