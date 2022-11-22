import re


def master_wordlist() -> list:
    f = open('WORD.LST', 'r')
    contents = f.read()
    f.close()

    wordlist = contents.split()
    return wordlist


def master_wordletters_dict() -> dict[str, list[str]]:
    """
    Dict{word: letters}
    :return: dict
    """
    wordlist = master_wordlist()

    wordletters_dict = {}
    for word in wordlist:
        letter_list = re.sub(r"([a-z])", r" \1", word).split()  # Separates strings by lowercase letter
        wordletters_dict[word] = letter_list  # "duck": ['d', 'u', 'c', 'k']

    return wordletters_dict


def master_wordsum_dict() -> dict[str, int]:
    """
    Dict{word: lettersum}
    :return: dict
    """
    wordletters_dict = master_wordletters_dict()

    wordsum_dict = {}
    for key in wordletters_dict:  # For each key in wordletters_dict
        add_together = 0
        for letter in key:  # And for every letter the key links to
            num = ord(letter) - 96  # Convert to number value
            add_together += num
        wordsum_dict[key] = add_together  # wordsum_dict["word": word sum]

    return wordsum_dict


def master_common_sumwords_dict() -> dict[int, list[str]]:
    """
    Dict{lettersum: [words]}
    :return: dict
    """
    wordsum_dict = master_wordsum_dict()

    common_sumword_dict: dict[int, list[str]] = {}
    for key in wordsum_dict:
        if wordsum_dict[key] in common_sumword_dict:
            common_sumword_dict[wordsum_dict[key]].append(key)
        else:
            common_sumword_dict[wordsum_dict[key]] = []

    return common_sumword_dict


def master_sumletter_dict() -> dict[int, list[str]]:
    wordletter_dict = master_wordletters_dict()
    wordsum_dict = master_wordsum_dict()

    # Make dict{lettersum: wordletter_dict}
    output = {}
    for key_word in wordsum_dict:  # output keys == wordsum_dict values
        output[wordsum_dict[key_word]] = []

    wordletter_item_list = list(wordletter_dict.values())
    for i in range(len(wordletter_item_list)):  # output values == wordletter_dict values
        output[i] = wordletter_item_list[i]

    return output








