# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def add_these_naiive(num_list: list[int], k: int):
    for i in num_list:
        for j in num_list:
            if i + j == k:
                return print("True")
    return print("False")


def add_these_1(num_list: list[int], k: int):
    num_list = sorted(num_list)
    pairs_list = []

    #[2, 3, 4, 6, 7, 8, 12]
    #12: +4

    for i in range(len(num_list)-1):
        temp_list = []

        if num_list[i] + num_list[i+1] < k:
            continue
        temp_list.append(num_list[i])
        temp_list.append(num_list[i+1])
        pairs_list.append(temp_list)

    i = 0
    while i < len(pairs_list):
        if sum(pairs_list[i]) > k:
            pairs_list.pop(i)
        else:
            i += 1

    if len(pairs_list) != 0:
        print("True")
        print(pairs_list)
    else:
        print("False")
        print(pairs_list)



def add_these(num_list: list[int], k: int):
    number_set = set()

    for num in num_list:
        if num not in number_set:
            number_set.add(num)

        difference = k - num
        if difference in number_set:
            print("True")
            return
    print("False")


add_these([15, 1, 7, 14], 17)






