def factorial_recursive(n):
    """
    Обчислює факторіал числа n рекурсивно.
    """
    if n < 0:
        raise ValueError("Число повинно бути невід'ємним!")
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
