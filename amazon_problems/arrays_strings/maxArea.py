class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_info = {}
        max = 0
        secmax = 0
        for i, h in enumerate(height):
        	if h > max:
        		max = h
        		max_info['max'] = (h, i)
        	elif h > secmax:
        		secmax = h
        		max_info['secmax'] = (h, i)

        print max_info
        print max_info['max']
        print max_info['secmax']
        print (abs(max_info['max'][1] - max_info['secmax'][1]))
        area = abs(max_info['max'][1] - max_info['secmax'][1]) * max_info['secmax'][0]
        print area


ob = Solution()
ob.maxArea([1,8,6,2,5,4,8,3,7])
