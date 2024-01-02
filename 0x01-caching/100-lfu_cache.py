#!/usr/bin/python3
"""class LFUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    This class represents a caching system using LFU algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.keys = []
        self.counts = {}

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data dictionary.

        Parameters:
        key (str): key where the item will be cached.
        item (str): the item to be cached.

        Returns:
        None
        """
        if key is None or item is None:
            return
        if key not in self.keys:
            self.keys.append(key)
        self.cache_data[key] = item
        self.counts[key] = self.counts.get(key, 0) + 1
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            least_freq = min(self.counts.values())
            least_freq_keys = [k for k, v in self.counts.items() if v == least_freq]
            if len(least_freq_keys) > 1:
                for k in self.keys:
                    if k in least_freq_keys:
                        discarded_key = k
                        break
            else:
                discarded_key = least_freq_keys[0]
            self.keys.remove(discarded_key)
            del self.cache_data[discarded_key]
            del self.counts[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        Parameters:
        key (str): key for which we need the value.

        Returns:
        str: Value linked to the key, None if key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.counts[key] += 1
        return self.cache_data[key]
