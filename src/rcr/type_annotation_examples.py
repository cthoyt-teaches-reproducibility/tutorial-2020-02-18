from typing import List


# This function shows how the semicolon can be used after the arguments
# in the definition of a function
def add_my_numbers(a: int, b: int) -> int:
    """This function adds two integers."""
    return a + b


# This example shows that a variadic arguments list using the splat operator
# should be annotated as having one type, and not as a list
def add_all_my_numbers(a: int, *numbers: int) -> int:
    return a + sum(numbers)


# Similar to the previous argument, this one takes a list that is not splatted.
# A helper class from the ``typing`` module is used to annotate the type of the
# list of numbers
def add_my_number_and_my_list_of_numbers(a: int, list_of_numbers: List[int]) -> int:
    return a + sum(list_of_numbers)
