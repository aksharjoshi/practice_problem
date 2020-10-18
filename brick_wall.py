class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        map = {}
        
        numRows, width = len(wall), sum(wall[0])

        for row in wall:
            sum_num=0
            for i,v in enumerate(row):
                sum_num += row[i]
                if sum_num in map:
                    map[sum_num] += 1
                else:
                    map[sum_num] = 1
        
        maxEnds = 0
        
        for key,value in map.iteritems():
            if(key!=width):
                maxEnds=max(maxEnds,value)

        return numRows-maxEnds