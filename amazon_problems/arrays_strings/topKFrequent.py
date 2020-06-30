class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
    
    # def topKFrequent(self, words, k):
    #     count = collections.Counter(words)
    #     heap = [(-freq, word) for word, freq in count.items()]
    #     heapq.heapify(heap)
    #     return [heapq.heappop(heap)[1] for _ in xrange(k)]