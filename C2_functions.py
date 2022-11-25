import re


def find_one_naiive(num: int):
    count = 0
    for i in range(0, num + 1):
        for j in str(i):
            if j == "1":
                count += 1
    return count


def get_int_at_index(num: int, index: int):
    return int(str(num)[index])


def find_one_complete(num: int):  # 152
    num_str = str(num)

    len_num = len(num_str)
    numbers = []
    for i in num_str:
        numbers.append(int(i))  # [1, 5, 2]
    for i in range(len_num):
        len_num -= 1
        for j in range(len_num):
            numbers[i] = numbers[i] * 10  # [100, 50, 2]

    count = 0
    for i in range(len(numbers)):
        numb = numbers[i]

        if numb == 0:
            continue

        if str(numb)[0] == "1":  # If num is in 100s place
            nines = find_one_nines(numb)  # Find nines
            other_numbers = sum(numbers[i+1:])
            nines += find_one_complete(other_numbers)
            return count + nines + other_numbers

        else:  # If first digit is over 1
            first_digit = get_int_at_index(numb, 0)
        # for 280  =       200 // 2        +             nines(200 // 2)                *      2
            count += (numb // first_digit) + ((find_one_nines(numb // first_digit) - 1) * first_digit)

    return count


def find_one_from(num1, num2):
    count = 0
    for i in range(num1, num2):
        for j in str(i):
            if j == "1":
                count += 1
    return count


def find_one_nines(num: int):
    num = str(num)

    digits = []
    for i in num:
        digits.append(int(i))  # ['1', '2', '3', '4', '5', '6']

    nines = 0
    for i in digits:  # For each digit
        nines = len(num) - 1
        for j in range(len(num) - 2):  # For len(num) - 2 times, nines * 10
            nines = nines * 10

    nines = nines + 1

    return nines























# def find_one(num: int) -> int:
#     string = str(num)
#
#     if len(string) == 1 and string != "0":  # If num is single digit and not 0, return 1
#         return 1
#
#     if len(string) > 1:  # If num is longer than 1
#
#         num_str = ""
#         # Adding 0s to mark 100s or 10s places in first of the sets of decimals
#         if len(string) % 3 == 2:
#             num_str = "0" + str(num)
#         if len(string) % 3 == 1:
#             num_str = "00" + str(num)
#
#         decimal_list = re.findall("...", num_str)
#
#
#         # Decimal_list = ["123", "456"]
#
#
#         count = 0
#         for decimals in decimal_list:
#             working_decimals = [int(decimals[0]), int(decimals[1]), int(decimals[2])]
#             if decimal_list[0]:
#
#                 ten = 2  # 1-10
#
#                 ones_above_twenty = 0  # Variable to count ones in 20-99
#                 if working_decimals[1] > 1:
#                     ones_above_twenty = working_decimals[1] - 2
#
#                 nines = 0
#                 if len(string) > 2:
#                     nines = len(string) - 1
#                     for i in range(len(string) - 2):
#                         nines = nines * 10
#
#                 tens = 0
#                 if len(string) > 1:
#                     tens = (ten + ones_above_twenty + find_one_naiive(working_decimals[2]))
#
#                 teens = 0
#                 hund_teens = 0
#                 if working_decimals[0] >= 1:
#                     hund_teens = 1 + tens
#                 if working_decimals[1] >= 1:
#                     teens = working_decimals[2]
#                 if working_decimals[1] >= 2:
#                     teens = 10
#
#                 count = hund_teens + teens + tens + nines
#         return count


def test_find_one(num):
    one = find_one_complete(num)
    naiive = find_one_naiive(num)
    print(f"{num}  fo: {one}  n: {naiive}")














