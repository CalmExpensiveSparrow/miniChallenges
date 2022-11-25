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

    if len(num_str) < 3:
        return find_one_naiive(num)

    numbers = []
    for i in num_str:
        numbers.append(int(i))  # [1, 5, 2]

    for i in range(len_num):
        len_num -= 1
        for j in range(len_num):
            numbers[i] = numbers[i] * 10

    # [100, 50, 2]

    count = 0
    for numb in numbers:
        current_count = 0

        if numb == 0:
            continue

        # If under 100, use naiive
        if len(numbers) < 3:
            return find_one_naiive(num)

        # If over 99
        if len(numbers) >= 3:
            if str(numb)[0] == "1" and len:  # If num in is 100s place, standard procedure
                # Works 100-1000
                nines = find_one_nines(numb)
                others = find_one_from(numb, numb+numbers[1]+numbers[2])  # This is the fucky one
                return count + nines + others

                # # for 280 =   200 // 2                       +           nines(200 // 2)                        *          2
                # count += (numb // get_int_at_index(numb, 0)) + ((find_one_base(numb // get_int_at_index(numb, 0))) * get_int_at_index(numb, 0))

            else:  # If first digit is more than 1
                if int(str(numb)[0]) >= 2:  # If first digit is 2
                 # for 280 =   200 // 2                          +           nines(200 // 2)                         *          2
                    count += (numb // get_int_at_index(numb, 0)) + ((find_one_base(numb // get_int_at_index(numb, 0))) * get_int_at_index(numb, 0))
                else:  # if above 2
                    count += find_one_nines(10 ** len(str(numb))) * 2
                    for i in range(len(str(numb))-2):
                        count += find_one_nines(10 ** len(str(numb)))
        print(count)
    return count

    # ten = 2  # 1-10
    #
    # ones_above_twenty = 0  # Variable to count ones in 20-99
    # if digits[1] > 1:
    #     ones_above_twenty = digits[1] - 2
    #
    # nines = 0
    # if len(num_str) > 2:
    #     nines = len(num_str) - 1
    #     for i in range(len(num_str) - 2):
    #         nines = nines * 10
    #
    # tens = 0
    # if len(num_str) > 1:
    #     tens = (ten + ones_above_twenty + find_one_naiive(digits[2]))
    #
    # teens = 0
    # hund_teens = 0
    # if digits[0] >= 1:
    #     hund_teens = 1 + tens
    # if digits[1] >= 1:
    #     teens = digits[2]
    # if digits[1] >= 2:
    #     teens = 10
    #
    # count = hund_teens + teens + tens + nines


def find_one_from(num1, num2):
    count = 0
    for i in range(num1, num2):
        for j in str(i):
            if j == "1":
                count += 1
    return count


def find_one_base(num: int):
    return find_one_nines(num) - 1


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














