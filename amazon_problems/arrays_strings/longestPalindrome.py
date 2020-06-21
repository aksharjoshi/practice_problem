class Solution(object):
    def longestPalindrome(self, s):
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m

    def longestPalindrome_old(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_len = 0
        palindrome = ''

        if len(s) == 1 or not s:
            return s

        for i, c in enumerate(s):
            temp = ''
            for ind, c1 in enumerate(s[i+1:]):
                temp += c1
                str_comp = c + temp
                #print c1
                reversed_str = ''.join(reversed(str_comp))
                if str_comp == reversed_str and len(str_comp) >= longest_len:
                    longest_len = len(str_comp)
                    palindrome = str_comp

        if not palindrome:
            return s[0]

        return palindrome

ob = Solution()
print ob.longestPalindrome("cbbd")
print ob.longestPalindrome("abcdedhbdghsk")