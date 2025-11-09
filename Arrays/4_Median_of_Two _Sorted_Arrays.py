class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        start, end = 0, m
        while start <= end:
            i = start + (end - start) // 2
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                end = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                start = i + 1
            else:
                max_left = nums1[i - 1] if j == 0 else (nums2[j - 1] if i == 0 else max(nums1[i - 1], nums2[j - 1]))
                if (m + n) % 2 == 1:
                    return max_left
                min_right = nums1[i] if j == n else (nums2[j] if i == m else min(nums1[i], nums2[j]))
                return (max_left + min_right) / 2
        return 1.0