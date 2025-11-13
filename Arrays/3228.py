class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            elif i > 0 and s[i-1] == '1':
                # We encountered a 0 that follows a 1 → this marks a zero-group barrier for all previous ones
                ans += ones
        return ans
