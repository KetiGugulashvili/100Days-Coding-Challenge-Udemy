# Random Password Generator
import random
import string
symbols_list = ['!', '@', '#', '$', '%', '&', '*', '(', ")", '+', '-', '=']
print("Welcome to the PyPassword Generator!")
letters = int(input("How many letter would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

password_elements = []
for i in range(0, letters):
    random_letter = random.choice(string.ascii_letters)
    password_elements.append(random_letter)

for i in range(0, numbers):
    random_number = random.randint(0, 10)
    password_elements.append(random_number)

for i in range(0, symbols):
    password_elements.append(random.choice(symbols_list))

password = ''
for i in range(0, len(password_elements)):
    random_for_list = random.randint(0, len(password_elements)-1)
    password += str(password_elements[random_for_list])
    password_elements.pop(random_for_list)

print(f"Here is your random password: {password}")


# exercise 1 - average heights
student_heights = input("Input a list of student heights: ").split(", ")
sum = 0
for i in student_heights:
    sum += int(i)
average = round(sum/len(student_heights))
print(f"The average height in the class is {average}")

# exercise 2 - highest in students
highest = 0
for i in student_heights:
    if int(i) > highest:
        highest = int(i)
print(f"The highest height in the class is {highest}")

# exercise 3 - sum even numbers
total = 0
for i in range(2, 101, 2):
    total += i
print(total)

# exercise 4 - FizzBuzz
number = 0
for i in range (1,101):
    number += 1
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)
