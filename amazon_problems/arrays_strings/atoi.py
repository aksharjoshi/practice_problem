class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            words = str.strip().split(' ')
            i = int(words[0])
            if(abs(i) > (2 ** 31)):
                if i > 0:
                    return (2 ** 31)
                else:
                    return -(2 ** 31)
            return i
        except Exception as e:
            return 0
        


ob = Solution()
print ob.myAtoi('   -42')
print ob.myAtoi("-91283472332")