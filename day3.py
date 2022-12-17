# exercise 1
weight = int(input("What's your weight? (in kg) "))
height = float(input("What's your height? (in m) "))
bmi = round(weight / height**2, 1)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you are a normal weight")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")

# exercise 2 - checking leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# exercise 3
size = input("What size pizza do you want? S, M, L? ")
add_peperoni = input("Do you want peperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
if size == "S":
    bill = 15
    print(f"Small pizza costs ${bill}")
    if add_peperoni == "Y":
        bill += 2
        print(f"Adding peperoni +2$")

if size == "M":
    bill = 20
    print(f"Medium pizza costs ${bill}")
    if add_peperoni == "Y":
        bill += 3
        print(f"Adding peperoni +3$")

if size == "L":
    bill = 25
    print(f"Large pizza costs ${bill}")
    if add_peperoni == "Y":
        bill += 3
        print(f"Adding peperoni +3$")

if extra_cheese == "Y":
    bill += 1
    print(f"Extra cheese +1$")

print(f"Your final bill is: ${bill}")

# exercise 4
print("Welcome to the love calculator.")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = name1+name2
name_lower_case = combined_name.lower()
true = "true"
love = "love"
sum1 = 0
sum2 = 0
for i in range(len(true)):
    sum1 += name_lower_case.count(true[i])
for i in range(len(love)):
    sum2 += name_lower_case.count(love[i])

print(f"Your score is {str(sum1)+str(sum2)}")

# exercise 5
print("Welcome to Treasure Island. Your mission is to find the treasure.")
first_move = input("You're at a cross road. Where do you want to go? type 'Left' or 'Right'\n")
if first_move == "Left":
    second_move = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat, or type 'swim' to swim across\n")
    if second_move == "wait":
        third_move = input("You arrive at the island unharmed. There is a house with 3 doors: red, yellow and blue. Which colour do you choose?\n")
        if third_move == "red":
            print("Burned by fire, game over")
        elif third_move == "blue":
            print("Eaten by beasts, game over")
        elif third_move == "yellow":
            print("You wiin!!!")
        else:
            print("Game over")
    else:
        print("Attacked by trout, game over")
else:
    print("Fall into a hole, game over")