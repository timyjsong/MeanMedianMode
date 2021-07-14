"""Module for Calculating Mean, Median, and Mode"""
from random import randint


class InvalidInputFormatException(BaseException):
    """Exception for Invalid Input Format"""

    def __str__(self):
        return "Input format is Invalid"


class EmptyListException(BaseException):
    """Exception for Empty List"""

    def __str__(self):
        return "Input list cannot be Empty"


def random_gen(size, lower=30, upper=50):
    """function to generate a list of random numbers with sizing as input"""

    return [randint(lower, upper) for _ in range(size)]


def mean(numbers):
    """mean function with list input"""

    if not isinstance(numbers, list):
        raise InvalidInputFormatException
    if len(numbers) == 0:
        raise EmptyListException

    # return round(sum(numbers) / len(numbers), 2)

    sum_float = 0.0
    for num in numbers:
        sum_float += num

    sum_float /= len(numbers)
    return round(sum_float, 2)


def median(numbers):
    """median function with list input"""

    if not isinstance(numbers, list):
        raise InvalidInputFormatException
    if len(numbers) == 0:
        raise EmptyListException

    sorted_numbers = sorted(numbers)
    index = len(numbers) // 2

    if len(numbers) % 2:
        # if odd
        ret_median = sorted_numbers[index]
    else:
        # if even
        middle_sum = sorted_numbers[index - 1] + sorted_numbers[index]
        ret_median = round(middle_sum / 2, 2)

    return ret_median


def mode(numbers):
    """mode function with list input"""

    if not isinstance(numbers, list):
        raise InvalidInputFormatException
    if len(numbers) == 0:
        raise EmptyListException

    count_dict = dict.fromkeys(set(numbers), 0)

    for num in numbers:
        count_dict[num] += 1

    max_count = sorted(count_dict.values(), reverse=True)[0]

    result_list = []
    for key, value in count_dict.items():
        if value == max_count:
            result_list.append(key)

    return result_list


def main():
    """main function"""

    numbers = random_gen(20, lower=30, upper=50)

    print(sorted(numbers))
    print("---------------------------------")
    print(f"Mean is : {mean(numbers)}")
    print(f"Median is : {median(numbers)}")
    print(f"Mode is : {mode(numbers)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
