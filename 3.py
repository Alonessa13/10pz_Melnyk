def sum_list_recursive(numbers):
    """
    Обчислює суму елементів списку рекурсивно.
    """
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_list_recursive(numbers[1:])
