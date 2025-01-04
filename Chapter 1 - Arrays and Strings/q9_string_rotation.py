def is_substring(s1, s2):

    rotation = ''
    for i in range(len(s1)):
        rotation = s1[i:] + s1[:i]

        if rotation == s2:
            return True
    return False


assert is_substring("waterbottle", "erbottlewat") is True
assert is_substring("waterbottle", "bottlewater") is True
assert is_substring("waterbottle", "rbottlewate") is True
