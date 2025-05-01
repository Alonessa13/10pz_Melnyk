def is_palindrome_recursive(s):
    """
    Перевіряє рекурсивно, чи є рядок паліндромом.
    """
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])
