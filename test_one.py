import one_a
import one_b


def test_sum_of_two_is_twenty_twenty():
    assert one_a.sum_of_two_numbers_is_twenty_twenty(2020, 0) == True
    assert one_a.sum_of_two_numbers_is_twenty_twenty(2020, 1234) == False


def test_iterate_and_calculate():
    assert one_a.iterate_and_calculate([2, 4, 51, 2000, 20]) == (2000, 20)
    assert one_a.iterate_and_calculate([2, 4, 51, 123, 20]) == None


# missing some coverage in 1a but most logic is tested at least


def test_sum_of_three_numbers_is_twenty_twenty():
    assert one_b.sum_of_three_numbers_is_twenty_twenty(2016, 0, 4) == True
    assert one_b.sum_of_three_numbers_is_twenty_twenty(2000, 19, 4) == False


def test_main_one_b_logic():
    list = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    assert (
        one_b.multiply_list_of_numbers(
            one_b.find_three_numbers_that_sum_to_twenty_twenty(list)
        )
        == 241861950,
        "One B logic Output",
    )


# iterate and calculate bad function name
# given recreated similar functions for 1a and 1b could have refactored so they handle larger number of argument to sum 2020
# with more time give function descrption/ more unit testing, make it command line runnable
