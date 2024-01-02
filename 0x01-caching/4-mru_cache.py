#!/usr/bin/python3
"""class MRUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    This class represents a caching system using MRU algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.keys = []

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
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache_data[key] = item
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys[-2]
            self.keys.remove(discarded_key)
            del self.cache_data[discarded_key]
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
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
