class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        #tmp = s[0]
        final_len = 1
        for i in range(0,len(s)):
            tmp = s[i]
            temp_len = 0
            for j in range(i+1, len(s)):
                if not s[j] in tmp:
                    tmp += s[j]
                    l = len(tmp)
                    if final_len < l:
                        final_len = l
                else:
                    l = len(tmp)
                    if final_len < l:
                        final_len = l
                    tmp = ''
                    break

            if temp_len > final_len:
                final_len = temp_len
        
        return final_len

s = Solution()
l = s.lengthOfLongestSubstring("au")
print l