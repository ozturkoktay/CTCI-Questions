'''

Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t


Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''


def one_edit_distance(string1, string2):
    one_way = []
    if len(string1) > len(string2):

        for i in range(len(string1)):
            for j in range(len(string2)):
                if string1[i] == string2[j]:
                    one_way.append(string1[j])
                else:
                    one_way.insert(i, string1[j])

        one_way = ''.join(one_way)
        print(one_way)
        if one_way == string1:
            return True
        else:
            return False
    else:
        print("aa")


assert one_edit_distance('pale', 'ple') is True
assert one_edit_distance('pales', 'pale') is True
# assert one_edit_distance('pale', 'bale') is True
# assert one_edit_distance('pale', 'bakes') is False
