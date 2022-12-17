# Hangman
import random
print("Guess a word!")
word_list = ["bamboo", "cat", "dog", "melon", "clock", "television", "mobile"]
# Choosing random word
random_word = random.choice(word_list)
word_list = list(random_word)

# Showing user number of letters
users_list =[]
for i in word_list:
    users_list.append("_")
print(users_list)

# Guessing a letter
lives = 5
while lives >= 0:
    users_guess = input("Guess a letter: ").lower()
# Check if the letter is in the word and if it is, add it in the list
    if random_word.count(users_guess) == 0:
        lives -= 1
    else:
        for i in range(len(word_list)):
            if word_list[i] == users_guess:
                users_list[i] = users_guess
# Check if user guessed the whole word
    if users_list == word_list:
        print(users_list)
        print("You won!")
        break
# Check if user have lives left
    print(users_list)
    if lives == 0:
        print("You lost! :(")
        break
    else:
        print(f"You have {lives} tries left.")