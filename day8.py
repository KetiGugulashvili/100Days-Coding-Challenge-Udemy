# Caesar Cipher
import string

alphabet = list(string.ascii_lowercase)


def change_letter(letter, number, encode):
    for i in range(0, len(alphabet)):
        if alphabet[i] == letter:
            if encode == "decode":
                number *= -1
            position = len(alphabet) - i - number
            if position > 0:
                letter = alphabet[i + number]
            else:
                letter = alphabet[-position]
            break

    return letter


def change_word(message, number, encode):
    message_list = list(message)
    for i in range(0, len(message_list)):
        message_list[i] = change_letter(message_list[i], number, encode)

    word = ''.join(message_list)
    return word


while True:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))
    print(f"Your {action}d message is {change_word(message, shift_number, action)}")
    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if go_again == "no":
        break

# exercise 1
import math


def cans_for_painting(h, w):
    return math.ceil((h * w) / 5)


height = int(input("Height of wall: "))
width = int(input("Width of wall: "))

print(f"You will need {cans_for_painting(height, width)} cans of paint")


# exercise 2 - Check prime number
def prime_checker(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print("It's not a prime number")
    else:
        print("It is a prime number")


number = int(input("Check this number: "))
prime_checker(number)


