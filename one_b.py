import os
import math


def sum_of_three_numbers_is_twenty_twenty(number_one, number_two, number_three):
    if number_one + number_two + number_three == 2020:
        return True
    else:
        return False


def find_three_numbers_that_sum_to_twenty_twenty(list_of_numbers):
    for i, number_one in enumerate(list_of_numbers):
        for j, number_two in enumerate(list_of_numbers):
            for k, number_three in enumerate(list_of_numbers):
                if i == k or i == j or j == k:
                    continue
                elif (
                    sum_of_three_numbers_is_twenty_twenty(
                        number_one, number_two, number_three
                    )
                    == True
                ):
                    return number_one, number_two, number_three


def multiply_list_of_numbers(list_of_numbers):
    return math.prod(list_of_numbers)


def main_one_1b():
    input_file = open("input/input1.txt", "r")

    lines = input_file.readlines()
    cleansed_lines = []
    for line in lines:
        cleansed_lines.append(int(line.replace("\n", "")))

    numbers_that_sum_to_twenty_twenty = find_three_numbers_that_sum_to_twenty_twenty(
        cleansed_lines
    )
    print(numbers_that_sum_to_twenty_twenty)
    product = multiply_list_of_numbers(numbers_that_sum_to_twenty_twenty)
    print(
        f"This is the product of two number that sum to twenty twenty! \nProduct: {product}"
    )
    return product


main_one_1b()
