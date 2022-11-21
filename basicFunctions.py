import re


def master_wordlist() -> list:
    f = open('WORD.LST', 'r')
    contents = f.read()
    f.close()

    wordlist = contents.split()
    return wordlist


def master_letter_dict():
    """
    Dict{word: letters}
    :return: dict
    """
    wordlist = master_wordlist()

    letter_dict = {}
    for word in wordlist:
        letter_list = re.sub(r"([a-z])", r" \1", word).split()  # Separates strings by lowercase letter
        letter_dict[word] = letter_list  # "duck": ['d', 'u', 'c', 'k']
    return letter_dict


def master_lettersum_dict():
    """
    Dict{word: lettersum}
    :return: dict
    """
    letter_dict = master_letter_dict()

    ascii_dict = {}
    for key in letter_dict:  # For each key in letter_dict
        add_together = 0
        for letter in key:  # And for every letter the key links to
            num = ord(letter) - 96  # Convert to number value
            add_together += num
        ascii_dict[key] = add_together  # ascii_dict["word": word sum]

    return ascii_dict


def master_common_lettersum_dict():
    """
    Dict{lettersum: [words]}
    :return: dict
    """
    ascii_dict = master_lettersum_dict()

    lettersum_dict = {"": []}
    for key in ascii_dict:
        if ascii_dict[key] in lettersum_dict:
            lettersum_dict[ascii_dict[key]].append(key)
        else:
            lettersum_dict[ascii_dict[key]] = []

    return lettersum_dict
