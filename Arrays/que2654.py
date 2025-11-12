from math import gcd
from collections import Counter

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        counter = Counter(nums)

        # If all numbers are already 1
        if counter[1] == n:
            return 0

        # If at least one 1 exists
        if counter[1] > 0:
            return n - counter[1]

        # Find the shortest subarray with GCD == 1
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break  # No need to continue once GCD = 1

        # If no subarray can make a 1
        if min_len == float('inf'):
            return -1

        # Total operations
        return (min_len - 1) + (n - 1)
