from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            if len(self.cache)== self.capacity:
                self.cache.popitem(last = False)
            self.cache[key] = value
            return
        # self.cache.move_to_end(key)
        least_used_value = self.cache.pop(key)
        self.cache[key] = value
        return
