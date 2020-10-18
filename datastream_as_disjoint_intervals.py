class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.len = len(self.arr)
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        # Remove duplicates
        self.arr = list(dict.fromkeys(self.arr))
        self.arr.sort()
        self.len = len(self.arr)
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        if self.len == 0:
            return -1
        if self.len == 1:
            return [[self.arr[0], self.arr[0]]]
        minimum = idx = -1
        ans = []
        for i, val in enumerate(self.arr):
            if i+1 == self.len and minimum == idx == -1:
                ans.append([self.arr[i], self.arr[i]])
                break
            elif i+1 == self.len:
                ans.append([self.arr[idx], self.arr[i]])
                break
            if self.arr[i+1] - val > 1 and minimum == idx == -1:
                ans.append([self.arr[i], self.arr[i]])
            elif self.arr[i+1] - val == 1:
                minimum = val if minimum == -1 else min(minimum, val)
                idx = i if idx == -1 else min(idx, i)
            else:
                ans.append([self.arr[idx], self.arr[i]])
                minimum = idx = -1
        return ans

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()