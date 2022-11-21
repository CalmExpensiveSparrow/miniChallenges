from basicFunctions import *
import re


#
#
# ---------------- Converts lowercase letters to their number position in the alphabet and sums them -------------------
def lettersum(string: str) -> int:
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


def sumletter(number: int):
    letter_dict = master_letter_dict()

    ascii_dict = {}
    for key in letter_dict:  # For each key in letter_dict
        add_together = 0
        for letter in key:  # And for every letter the key links to
            num = ord(letter) - 96  # Convert to number value
            add_together += num
            if add_together > number:  # If word sum is higher than number, break
                break
        if add_together > number:  # Break2: Electric Boogaloo: not Break
            continue
        ascii_dict[key] = add_together  # ascii_dict["word": word sum]

    key_list = []
    for key in ascii_dict:
        if ascii_dict[key] == number:
            key_list.append(key)

    for key in key_list:
        print(f"{key}, ", end="")
    print(len(key_list))


def xxx(number: int):
    wordlist = master_wordlist()

    results = []
    for word in wordlist:
        if lettersum(word) == number:
            results.append(word)

    for key in results:
        print(key)


def odd_sumletter():
    ascii_dict = master_lettersum_dict()

    odd_sum_list = []
    for key in ascii_dict:
        if ascii_dict[key] % 2 != 0:
            odd_sum_list.append(key)

    for key in odd_sum_list:
        print(f"{key}, ", end="")
    print(len(odd_sum_list))


def most_common_lettersum():
    ascii_dict = master_lettersum_dict()

    most_common = 0
    num_common = 0
    for base_key in ascii_dict:
        maybe_key = 0
        maybe_count = 0
        for sum_key in ascii_dict:
            if ascii_dict[sum_key] == ascii_dict[base_key]:
                maybe_key = ascii_dict[base_key]
                maybe_count += 1

        if num_common < maybe_count:
            most_common = maybe_key
            num_common = maybe_count

        if base_key == "zyzzyvas":
            return print(most_common, num_common)
#  ---------------------------------------------------------------------------------------------------------------------






















