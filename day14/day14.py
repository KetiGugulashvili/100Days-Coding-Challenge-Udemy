from data import data
import random


def checking_answer(A, B, guess):
    if A['follower_count'] > B['follower_count']:
        return guess == "a"
    else:
        return guess == "b"


def printing_people(A, B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")


B = random.choice(data)
current_score = 0

while True:
    A = B
    B = random.choice(data)
    while A == B:
        B = random.choice(data)
    printing_people(A, B)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if checking_answer(A, B, guess):
        current_score += 1
        print(f"You're right! Current Score: {current_score}")
    else:
        print(f"Sorry, that's wrong. Final score {current_score}")
        break
