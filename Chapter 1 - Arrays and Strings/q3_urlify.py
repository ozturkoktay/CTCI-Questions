"""
Write a method to replace all the spaces in a string with ‘%20’. You may assume that the string has sufficient space at the end to hold the additional characters and that you are given the “true” length of the string.

Examples: 
Input: "Mr John Smith", 13
Output: Mr%20John%20Smith

Input: "Mr John Smith   ", 13
Output: Mr%20John%20Smith
"""

# Solution using strip and replace methods


def replace_spaces(str):
    return str.strip().replace(' ', '%20')


assert replace_spaces('Mr John Smith') == 'Mr%20John%20Smith'
assert replace_spaces('Mr John Smith   ') == 'Mr%20John%20Smith'


# Solution without using Python fuctions

def no_magic_replace_spaces(input_str):

    url = []
    n = len(input_str)

    for i in range(n):
        if input_str[i] == ' ':
            if i + 1 < n and input_str[i + 1].isalpha():
                url.append('%20')
            elif i + 1 == n:
                continue
        else:
            url.append(input_str[i])

    return ''.join(url)


assert no_magic_replace_spaces('Mr John Smith') == 'Mr%20John%20Smith'
assert no_magic_replace_spaces('Mr John Smith   ') == 'Mr%20John%20Smith'
