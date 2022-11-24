import re

def find_one_naiive(num: int):
    count = 0
    for i in range(0, num + 1):
        for j in str(i):
            if j == "1":
                count += 1
    return count

def find_one(num: int) -> int:
    string = str(num)

    if len(string) == 1 and string != "0":  # If num is single digit and not 0, return 1
        return 1

    if len(string) > 1:  # If num is longer than 1

        num_str = ""
        # Adding 0s to mark 100s or 10s places in first of the sets of decimals
        if len(string) % 3 == 2:
            num_str = "0" + str(num)
        if len(string) % 3 == 1:
            num_str = "00" + str(num)

        decimal_list = re.findall("...", num_str)  # ["654", "321"]


        # Decimal_list = ["123", "456"]


        count = 0
        for decimals in decimal_list:
            working_decimals = [int(decimals[0]), int(decimals[1]), int(decimals[2])]
            if decimal_list[0]:

                ten = 2  # 1-10

                ones_above_twenty = 0  # Variable to count ones in 20-99
                if working_decimals[1] > 1:
                    ones_above_twenty = working_decimals[1] - 2

                nines = 0
                if len(string) > 2:
                    nines = len(string) - 1
                    for i in range(len(string) - 2):
                        nines = nines * 10

                tens = 0
                if len(string) > 1:
                    tens = (ten + ones_above_twenty + find_one_naiive(working_decimals[2]))

                teens = 0
                hund_teens = 0
                if working_decimals[0] >= 1:
                    hund_teens = 1 + tens
                if working_decimals[1] >= 1:
                    teens = working_decimals[2]
                if working_decimals[1] >= 2:
                    teens = 10

                count = hund_teens + teens + tens + nines
        return count


def test_find_one(num):
    one = find_one(num)
    naiive = find_one_naiive(num)
    print(f"{num}  fo: {one}  n: {naiive}")














