# Blackjack
import random
from replit import clear


def winner_reveal(list1, list2):
    """Reveals a winner using sum of lists."""
    if sum(list1) > 21:
        return "You lose :( Your cards are more than 21."
    elif sum(list2) > 21:
        return "You win, computer's cards are more than 21."
    elif list2 == 0:
        return "You lose, opponent has Blackjack :("
    elif list1 == 0:
        return "You win with a Blackjack."
    elif sum(list1) > sum(list2):
        return "You win!"
    elif sum(list1) < sum(list2):
        return "You lose :( Computer has higher number."
    elif sum(list1) == sum(list2):
        return "It's a draw."
    else:
        return "Error"


def random_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def play_game():
    user_cards = [random_card(), random_card()]
    computers_cards = [random_card(), random_card()]
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computers_cards[0]}")
    while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        if sum(computers_cards) < 17:
            computers_cards.append(random_card())
        elif sum(computers_cards) == 21:
            print("You lose, opponent has Blackjack :(")
            break
        user_cards.append(random_card())
        print(f"Your cards: {user_cards}")

    print(f"You final hand: {user_cards}\nComputer's final hand: {computers_cards}")
    print(winner_reveal(user_cards, computers_cards))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
