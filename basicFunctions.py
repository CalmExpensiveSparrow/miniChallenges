import re


def master_wordlist() -> list:
    f = open('WORD.LST', 'r')
    contents = f.read()
    f.close()

    wordlist = contents.split()
    return wordlist


def master_letter_dict():
    wordlist = master_wordlist()

    letter_dict = {}
    for word in wordlist:
        letter_list = re.sub(r"([a-z])", r" \1", word).split()  # Separates strings by lowercase letter
        letter_dict[word] = letter_list  # "duck": ['d', 'u', 'c', 'k']
    return letter_dict


def master_lettersum_dict():
    letter_dict = master_letter_dict()

    ascii_dict = {}
    for key in letter_dict:  # For each key in letter_dict
        add_together = 0
        for letter in key:  # And for every letter the key links to
            num = ord(letter) - 96  # Convert to number value
            add_together += num
        ascii_dict[key] = add_together  # ascii_dict["word": word sum]

    return ascii_dict
