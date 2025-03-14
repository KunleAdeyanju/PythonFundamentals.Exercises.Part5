def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value_reversed = value[::-1].replace(" ", "").lower()
    return (value.replace(" ", "").lower() == value_reversed)  # remove pass statement and implement me
