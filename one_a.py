import os


def sum_of_two_numbers_is_twenty_twenty(number_one, number_two):
    if number_one + number_two == 2020:
        return True
    else:
        return False


def iterate_and_calculate(list_of_numbers):
    for i, number_one in enumerate(list_of_numbers):
        for j, number_two in enumerate(list_of_numbers):
            if i == j:
                continue
            elif sum_of_two_numbers_is_twenty_twenty(number_one, number_two) == True:
                return number_one, number_two


def multiply_two_numbers(number_one, number_two):
    return number_one * number_two


def main_one_1a():
    input_file = open("input/input1.txt", "r")

    lines = input_file.readlines()
    cleansed_lines = []
    for line in lines:
        cleansed_lines.append(int(line.replace("\n", "")))

    numbers_that_sum_to_twenty_twenty = iterate_and_calculate(cleansed_lines)
    product = multiply_two_numbers(
        numbers_that_sum_to_twenty_twenty[0], numbers_that_sum_to_twenty_twenty[1]
    )
    print(
        f"This is the product of two number that sum to twenty twenty! \nProduct: {product}"
    )
    return product


main_one_1a()
