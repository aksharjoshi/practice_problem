def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        finalnums = nums1
        for i in range(0, len(nums2)):
            finalnums.append(nums2[i])
        
        finalnums.sort()
        finallen = len(finalnums)
        print "finalnums = ", finalnums
        median = 0.0
        
        if finallen % 2 == 0:
            print finalnums[finallen/2 - 1]
            print finalnums[finallen/2]
            print (finalnums[finallen/2 - 1] + finalnums[finallen/2])
            print (float(finalnums[finallen/2 - 1] + finalnums[finallen/2])/2)
            median = float(finalnums[finallen/2 - 1] + finalnums[finallen/2]) / 2
            print "median in mod = ", median
        else:
            median = finalnums[finallen/2]
            print "median in non mod = ", median
        
#         lenfinal = len1 if len1 >= len2 else len2
#         print "lenfinal = ", lenfinal
        
#         median = (lenfinal + 1) / 2
        
#         #return "The median is " + str(median)
        return median



findMedianSortedArrays([1,2],[3,4])