class Solution(object):
    def findFinalValue(self, nums, original):
        i=0
        nums.sort()
        while i <len(nums):
            if nums[i]==original:
                original=original*2
                i=0
                continue
            i+=1
        return original
        


class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
                original *= 2
        return(original)