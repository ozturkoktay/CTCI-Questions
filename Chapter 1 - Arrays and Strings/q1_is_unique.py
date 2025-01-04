"""
Q: Implement an algorithm to determine if a string has all unique characters.

Examples:

Input : abcd10jk
Output : true

Input : hutg9mnd!nk9
Output : false

"""


# Brute Force Solution: O(n^2)
def is_unique(text: str):
    for i in range(len(text) - 1):
        for j in range(i + 1, len(text) - 1):
            if text[i] == text[j]:
                return False

    return True


assert is_unique('abcd10jk') is True
assert is_unique('hutg9mssssnd!nk9') is False
assert is_unique('hutg9mnd!nk9') is False


# Solution with set: O(n)
def is_unique_set(text: str):
    unique_string = set()

    for t in text:
        if t in unique_string:
            return False
        else:
            unique_string.add(t)
    return True


assert is_unique_set('abcd10jk') is True
assert is_unique_set('hutg9mssssnd!nk9') is False
assert is_unique_set('hutg9mnd!nk9') is False
