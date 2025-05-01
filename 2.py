def fibonacci_recursive(n):
    """
    Обчислює n-те число Фібоначчі рекурсивно.
    """
    if n < 0:
        raise ValueError("Число повинно бути невід'ємним!")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
