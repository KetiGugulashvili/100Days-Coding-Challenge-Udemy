# Number Guessing Game!
def checking_the_number(correct, guess):
    if guess > correct:
        return "Too high."
    if guess < correct:
        return "Too low."
    if guess == correct:
        return f"You got it! The answer was {correct}"

from random import randint
random_num = randint(1, 100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number_of_guess = input("Choose a difficulty. Type 'easy' or 'hard': ")
if number_of_guess == "easy":
    number_of_guess = 10
elif number_of_guess == "hard":
    number_of_guess = 5

for i in range(number_of_guess):
    print(f"You have {number_of_guess-i} attempts remaining to guess the number")
    guess_number = int(input("Make a Guess: "))
    print(checking_the_number(random_num, guess_number))
    if random_num != guess_number and i == number_of_guess-1:
        print("You lose. You're out of attempts.")
    else:
        print("Guess Again.")
    if random_num == guess_number:
        break

