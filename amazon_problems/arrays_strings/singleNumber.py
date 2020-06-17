class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                non_repeat = nums[i]
                break
        if i < len(nums):
            non_repeat = nums[i]
        
        return non_repeat
        