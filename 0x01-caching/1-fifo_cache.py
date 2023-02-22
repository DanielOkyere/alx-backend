#!/usr/bin/env python3
""" 1-fifo_cache """
from collections import OrderedDict
baseCache = __import__('base_caching').BaseCaching


class FIFOCache(baseCache):
    """Class FIFOCache inherits BaseCachin"""
    def __init__(self):
        """Init function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put method on FIFOCache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > baseCache.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve from cache"""
        return self.cache_data.get(key, None)
