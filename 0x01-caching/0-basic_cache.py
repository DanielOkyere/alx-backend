#!/usr/bin/env python3
""" 0-basic_cache """


base_caching = __import__('base_caching').BaseCaching


class BasicCache(base_caching):
    """ Class BasicCache inherits base caching"""
    def put(self, key, item):
        """put key in cache_data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
