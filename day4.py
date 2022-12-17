# exercise 1
import random
coin = random.randint(0, 1)
if coin == 0:
    print("Tails")
else:
    print("Heads")

# exercise 2
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# v1
random_name_index = random.randint(0, len(names)-1)
print(f"{names[random_name_index]} is paying for the meal today!")
# v2
print(f"{random.choice(names)} is paying for the meal today!")

# exercise 3
row1 = ["😊", "😊", "😊"]
row2 = ["😊", "😊", "😊"]
row3 = ["😊", "😊", "😊"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure? (column, row) ")
map[int(position[1])-1][int(position[0])-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")

# exercise 4 - Rock, Paper, Scissors
move1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game = ["Rock", "Paper", "Scissors"]
print(f"You chose {game[move1]}")
move2 = random.randint(0, 2)
print(f"Computer chose {game[move2]}")
if move1 >= 3 or move1 < 0:
    print("Invalid number, you lose!")
elif move2 == 0 and move1 == 2:
    print("You lose!")
elif move1 == move2:
    print("It's a tie")
elif move1 == 0 and move2 == 2:
    print("You win!")
elif move1 > move2:
    print("You win!")
elif move2 > move1 :
    print("You lose!")
else:
    print("Error")
