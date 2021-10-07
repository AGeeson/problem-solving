string2 = "1-3 a: abcde"


def split_into_multiple_args(string):
    string = string.split()
    range_of_instances = [int(x) for x in string[0].split("-")]
    context = {
        "given_numbers": range_of_instances,
        "main_character": string[1].replace(":", ""),
        "output_string": string[2],
    }
    return context


def iterate_through_string_and_count_instances_of_character(string, character):
    i = 0
    for letter in string:
        if letter == character:
            i += 1
    return i


def is_number_in_range(number, range):
    if number >= range[0] and number <= range[1]:
        print(f"{number} is in range of {range[0]} and {range[1]}! Hurrah!")
        return True
    else:
        print(f"{number} is NOT n range of {range[0]} and {range[1]}! Boo!")
        return False


def character_is_in_a_correct_position(positions, character, string):
    for index, letter in enumerate(string):
        position = index + 1
        if character == letter and position in positions:
            return True


def logic_per_line_two_a(line):
    context = split_into_multiple_args(line)
    instances = iterate_through_string_and_count_instances_of_character(
        context["output_string"], context["main_character"]
    )
    return is_number_in_range(instances, context["range_of_instances"])


def log_per_line_two_b(line):
    context = split_into_multiple_args(line)
    return character_is_in_a_correct_position(
        context["given_numbers"],
        context["main_character"],
        context["output_string"],
    )


def how_many_lines_of_file_meet_conditional(conditional):
    input_file = open("input/input2.txt", "r")

    lines = input_file.readlines()
    times_conditional_met = 0
    for line in lines:
        if conditional(line) == True:
            times_conditional_met += 1
    print(times_conditional_met)
    return times_conditional_met


# for 2a... how_many_lines_of_file_meet_conditional(logic_per_line_two_a)
# for 2b... how_many_lines_of_file_meet_conditional(log_per_line_two_b)
