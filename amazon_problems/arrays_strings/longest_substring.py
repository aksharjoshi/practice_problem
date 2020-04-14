class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setch = set()
        ans = i = j = 0
        n = len(s)
        while i < n and j < n:
        	if not s[j] in setch:
        		setch.add(s[j])
        		j += 1
        		ans = max(ans, j-i)
        	else:
        		setch.remove(s[i])
        		i += 1
        return ans

ob = Solution()
print ob.lengthOfLongestSubstring('abcajshshs')