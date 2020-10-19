class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        stack = []
        for char in s:
            if char == "(":
                stack.append([])
            elif char == ")":
                if len(stack) == 1:
                    res += "".join(stack.pop()[::-1])
                    continue
                word = stack[-1][::-1]
                stack.pop()
                stack[-1] += word           
            else:
                if stack:
                    stack[-1].append(char) 
                else:
                    res+= char       
        return res