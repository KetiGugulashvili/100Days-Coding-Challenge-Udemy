with open("Input/Names/invited_names.txt", "r") as file:
    guests = file.readlines()


with open("Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

for guest in guests:
    with open(f"Output/letter_to_{guest[:-1]}.txt", "w") as file:
        new_letter = letter.replace("[name]", guest[:-1])
        file.write(new_letter)
