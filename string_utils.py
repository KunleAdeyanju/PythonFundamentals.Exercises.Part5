
def str_len(str_in: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    return len(str_in) # remove pass statement and implement me


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    return str_in[0]  # remove pass statement and implement me


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    return str_in[-1]  # remove pass statement and implement me


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    return sub_str_in in str_in  # remove pass statement and implement me


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    return str_in[start:stop]  # remove pass statement and implement me


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """

    # str_in_reversed = str_in[::-1]
    str_in_list = list(str_in)
    str_in_r = ""

    for i in range(len(str_in_list)):
        if str_in_list[i].isupper():
            str_in_list[i] = str_in_list[i].lower()
        else:
            str_in_list[i] = str_in_list[i].upper()

        
    #return str_in_r.join(str_in_list)  my way worked well but like...
    return str_in.swapcase()