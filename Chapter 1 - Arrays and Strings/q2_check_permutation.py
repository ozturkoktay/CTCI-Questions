"""
Given two strings s1 and s2, return true if s2 contains a  permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


# ord takes the single character and return its unicode

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    # Initialize character counts for s1 and the sliding window
    s1_count = [0] * 26
    window_count = [0] * 26

    for char in s1:
        s1_count[ord(char) - ord('a')] += 1

    for i in range(len(s1)):
        window_count[ord(s2[i]) - ord('a')] += 1

    # Check the first window
    if s1_count == window_count:
        return True

    # Slide the window over s2
    for i in range(len(s1), len(s2)):
        start_char = s2[i - len(s1)]
        end_char = s2[i]

        window_count[ord(end_char) - ord('a')] += 1
        window_count[ord(start_char) - ord('a')] -= 1

        if s1_count == window_count:
            return True

    return False
