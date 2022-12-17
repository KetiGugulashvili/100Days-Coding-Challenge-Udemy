# exercise 1
integer = input("Type the integer: ")
sum = 0
for i in range(len(integer)):
    sum += int(integer[i])

print(sum)

# exercise 2
weight = int(input("What's your weight? (in kg) "))
height = float(input("What's your height? (in m) "))
bmi = round(weight / height**2, 1)
print(f"Your BMI is {bmi}")

# exercise 3
age = input("What is your current age? ")
years = 90 - int(age)
months = years*12
weeks = years*52
days = years*365
print(f"You have {days} days, {weeks} weeks, {months} months left.")

# tip calculator
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
total_payment = float(bill) + float(bill) * int(tip) / 100
payment_each = round(total_payment / int(people), 2)
print(f"Each person should pay: ${payment_each}")



