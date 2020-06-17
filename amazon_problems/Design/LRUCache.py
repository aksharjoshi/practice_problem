from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        super(LRUCache, self).__init__()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key, value)
        else:
            if len(self) >= self.capacity:
                self.popitem(last=False)
            self[key] = value
    
    def move_to_end(self, key, value=None):
        if not value:
            val = self[key]
            self.pop(key)
            self[key] = val
        else:
            self.pop(key)
            self[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# print obj
# print obj.put(1,1)
# print obj.put(2,2)
# print obj.get(1)
# print obj.put(3,3)
# print obj.get(2)
# print obj.put(4,4)
# print obj.get(1)
# print obj.get(3)
# print obj.get(4)