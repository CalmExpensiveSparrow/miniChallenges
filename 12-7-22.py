import numpy as numpy
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If the input was [3, 2, 1], the output would be
# [2, 3, 6].

# Follow-up: What if you couldn't use division?

# def multiply_naiive1(input_list: list):
#     output_list = []
#     temp_list = []
#
#     for i in input_list:
#         for j in input_list:
#             temp_list.append(j)
#         temp_list.remove(i)
#         output_list.append(numpy.prod(temp_list))
#         temp_list = []
#
#     print(output_list)


def multiply_naiive2(input_list: list):
    output_list = []
    temp_list = []

    for j in input_list:
        temp_list.append(j)

    for i in range(len(input_list)):
        temp_list.remove(input_list[i])
        output_list.append(numpy.prod(temp_list))
        temp_list.insert(i, input_list[i])

    print(output_list)


def multiply_naiive3(input_list: list):
    total = numpy.prod(input_list)

    output_list = []
    for i in range(len(input_list)):
        output_list.append(1)

    for i in range(len(output_list)):
        output_list[i] = output_list[i] * total // input_list[i]

    print(output_list)


multiply_naiive3([1, 2, 3, 4, 5])

