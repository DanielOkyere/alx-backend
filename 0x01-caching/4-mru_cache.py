#!/usr/bin/env python3
""" 1-fifo_cache """
from collections import OrderedDict
baseCache = __import__('base_caching').BaseCaching


class MRUCache(baseCache):
    """Class MRUCache inherits BaseCachin"""
    def __init__(self):
        """Init function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put method on LifoCache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > baseCache.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve from cache"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
