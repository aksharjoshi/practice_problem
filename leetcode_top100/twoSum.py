class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, value in enumerate(nums):
            remaining = target - value
            if(remaining in map):
                return [index, map[remaining]]
            
            map.update({value:index})
        raise Exception("No solution found")