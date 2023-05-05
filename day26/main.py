import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name = input("Enter a word: ")
    try:
        name_words = [data_dict[letter.upper()] for letter in list(name)]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(name_words)


generate_phonetic()