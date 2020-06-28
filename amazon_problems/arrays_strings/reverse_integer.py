class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            reverse = int(str(x)[::-1]) 
        else: 
            reverse = (-1 * int( str(x*-1)[::-1]))
        
        # handle 32 bit overflow  
        mina = -2**31  
        maxa = 2**31 - 1
        if not mina <= reverse <= maxa:  
            return 0  
        else:  
            return reverse