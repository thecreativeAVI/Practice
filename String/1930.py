class Solution:
    def countPalindromicSubsequence(self, s):
        # record first and last position of each character
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        result = 0

        # for each possible outer character
        for ch in first:
            if first[ch] < last[ch]:  # must have room for a middle character
                l = first[ch]
                r = last[ch]
                middle_chars = set(s[l+1 : r])  # unique characters in the middle
                result += len(middle_chars)

        return result
