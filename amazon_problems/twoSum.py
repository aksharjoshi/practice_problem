class Solution(object):
    def twoSum_brute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        remaining = target - nums[0]
        if remaining in nums[1:]:
        	ind = nums.index(remaining, 1, len(nums))
        	return [0, ind]


        for num in range(1, len(nums)-1):
        	remaining = target - nums[num]
        	if remaining in nums[num+1:]:
        		print 'remaining = ', remaining
        		print 'num = ', num
        		print nums.index(remaining, num+1, len(nums))
        		ind = nums.index(remaining, num+1, len(nums))
        		return [num, ind]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for num in range(0, len(nums)):
        	remaining = target - nums[num]
        	if remaining in maps:
        		return [num, maps[remaining]]
        	else:
        		maps.update({nums[num]: num})


ob = Solution()
print ob.twoSum([2,7,11,15], 9)
print ob.twoSum([3,3], 6)
print ob.twoSum([1,3,4,2], 6)
print ob.twoSum([2,5,5,11],10)