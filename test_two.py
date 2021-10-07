import two


def test_split_into_multiple_args():
    string = "1-3 a: abcde"
    assert two.split_into_multiple_args(string) == {
        "given_numbers": [1, 3],
        "main_character": "a",
        "output_string": "abcde",
    }


def test_iterate_through_string_and_count_instances_of_character():
    assert (
        two.iterate_through_string_and_count_instances_of_character("racecar", "c") == 2
    )


def test_is_number_in_range():
    assert two.is_number_in_range(2, [1, 4]) == True
    assert two.is_number_in_range(5, [7, 10]) == False


def test_logic_per_line_two_a():
    one_line_true = "1-3 a: abcde"
    one_line_false = "2-3 a: abcde"
    assert two.logic_per_line_two_a(one_line_true) == True
    assert two.logic_per_line_two_a(one_line_false) == False


def test_character_is_in_correct_positions():
    two.character_is_in_a_correct_position([1, 3], "a", "abcde") == True
    two.character_is_in_a_correct_position([2, 3], "a", "abcde") == False
    two.character_is_in_a_correct_position([5, 1], "t", "cccctddddd") == True
