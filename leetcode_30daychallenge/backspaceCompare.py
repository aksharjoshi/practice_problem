class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        import re
        countS = S.count('#')
        print countS
        countT = T.count('#')
        print countT, "\n\n"
        
        for i in range(0,countS):
            print i
            S = re.sub('(.)#', '', S)
            print S
        
        for j in range(0,countT):
            print j
            T = re.sub('(.)#', '', T)
            print T

        if '#' in T:
            T = T.replace('#','')
        if '#' in S:
            S = S.replace('#', '')

        if S == T:
            return True
        else:
            return False


ob = Solution()
#print ob.backspaceCompare("ab##", "c#d#")
#print ob.backspaceCompare("y#fo##f", "y#f#o##f")
print ob.backspaceCompare("du###vu##v#fbtu", "du###vu##v##fbtu")
        