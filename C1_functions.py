from C1_helper_functions import *
import re


#
#
# ---------------- Converts lowercase letters to their number position in the alphabet and sums them -------------------
def get_word_to_sum(string: str) -> int:
    """
    This function takes var string, converts the lowercase letters to number values, and adds them together
    :param string: Characters used to sum letter values
    :return: Summed letter values
    """
    input_list = re.sub(r"([a-z])", r" \1", string).split()  # Separates string by lowercase letter

    word = []
    for letter_string in input_list:
        if len(letter_string) > 1:
            letter_string = letter_string[0]
        word.append(letter_string)

    ascii_num = []
    for letter in word:
        ascii_num.append(ord(letter) - 96)

    return sum(ascii_num)
    # print(sum(ascii_num))


def get_sum_to_word_total(number: int) -> int:
    wordletters_dict = master_wordletters_dict()

    wordsum_dict = {}
    for key in wordletters_dict:  # For each key in wordletters_dict
        add_together = 0
        for letter in key:  # And for every letter the key links to
            num = ord(letter) - 96  # Convert to number value
            add_together += num
            if add_together > number:  # If word sum is higher than number, break
                break
        if add_together > number:  # Break2: Electric Boogaloo: not Break
            continue
        wordsum_dict[key] = add_together  # wordsum_dict["word": word sum]

    key_list = []
    for key in wordsum_dict:
        if wordsum_dict[key] == number:
            key_list.append(key)

    for key in key_list:
        print(f"{key}, ", end="")

    return len(key_list)


def xxx(number: int):
    wordlist = master_wordlist()

    results = []
    for word in wordlist:
        if get_word_to_sum(word) == number:
            results.append(word)

    for key in results:
        print(key)


def get_odd_sum_total() -> int:
    ascii_dict = master_wordsum_dict()

    odd_sum_list = []
    for key in ascii_dict:
        if ascii_dict[key] % 2 != 0:
            odd_sum_list.append(key)

    for key in odd_sum_list:
        print(f"{key}, ", end="")
    return len(odd_sum_list)


def most_common_sum_count():
    wordsum_dict = master_wordsum_dict()

    common_sumword_dict = {}
    for key in wordsum_dict:
        if wordsum_dict[key] in common_sumword_dict:  # if wordsum value is in dict
            common_sumword_dict[wordsum_dict[key]] += 1  # Add one to dict value
        else:
            common_sumword_dict[wordsum_dict[key]] = 1  # Add to dict

    highest_count = 0
    highest_value = 0
    for key in common_sumword_dict:
        if common_sumword_dict[key] > highest_count:  # if common_sumword_sict value is higher than the value in highest_count
            highest_count = common_sumword_dict[key]  # set highest_count to common_sumword_dict value
            highest_value = key  # highest value is the value's key

    print(f"{highest_value}: {highest_count}")

    # most_common_value = 0
    # most_common_count = 0
    # for base_key in wordsum_dict:
    #     base_key_value = 0
    #     base_key_count = 0
    #     for sum_key in wordsum_dict:
    #         if wordsum_dict[sum_key] == wordsum_dict[base_key]:
    #             base_key_value = wordsum_dict[base_key]
    #             base_key_count += 1
    #
    #     if most_common_count < base_key_count:
    #         most_common_value = base_key_value
    #         most_common_count = base_key_count
    #
    #     if most_common_value == 100:
    #         return print(most_common_value, most_common_count)


def get_word_length_pairs_by_common_sum(_sum: int):
    """
    Finds words with same lettersum and an eleven letter difference
    """
    common_dict = master_common_sumwords_dict()

    common_sumwords_dict = common_dict[_sum]

    # common_sumwords_dict = []
    # for key_lettersum in common_dict: # For every key in common_dict
    #     if key_lettersum == letter_sum:  # If the key matches the inputted letter_sum
    #         for word in common_dict[key_lettersum]:
    #             common_sumwords_dict.append(word)  # Put the words in the key list in the pairs list

    # pairs_dict = {}
    # for word in common_sumwords_dict:  # For each word in common_sumwords_dict list, get length of word
    #     word_len = len(word)
    #     for other_word in common_sumwords_dict:  # For each key in pairs_dict, get length of other_word
    #         other_word_len = len(other_word)
    #         if word_len - other_word_len == 11:  # if word_len and other_word_len have a difference of 11, add pair
    #             pairs_dict[other_word] = word
    #
    # print(pairs_dict)

    # TODO: make this not n^2
    pairs_dict = {}
    for i in range(len(common_sumwords_dict)):
        word = common_sumwords_dict[i]
        word_len = len(word)
        for j in range(i + 1, len(common_sumwords_dict)):
            other_word = common_sumwords_dict[j]
            other_word_len = len(other_word)
            if abs(word_len - other_word_len) == 11:
                pairs_dict[other_word] = word

    print(pairs_dict)


def uncommon_letter_common_sum_pairs() -> dict[str, str]:  # dict[word, word]
    """
    Returns word pairs that have the same sum, but no letters in common
    """
    sumletters_dict = master_sumletter_dict()  # dict[sum: [letters]]
    wordletters_dict = master_wordletters_dict()  # dict[word: [letters]]
    # dict[sum, [letters]]

    uncommon_letters_dict: dict[str, str] = {}  # dict[word, word]
    for sum_key in sumletters_dict:
        pass
#  ---------------------------------------------------------------------------------------------------------------------






















