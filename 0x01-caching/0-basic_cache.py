#!/usr/bin/python3
"""Class BasicCache that inherits from BaseCaching and is a caching sys"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    This class represents a basic caching system.
    """
    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data dict

        Parameters:
            key (str): Key where the item will be cached
            item (str): the item to be cached.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        retyrn the value in self.cache_data linked to key

        Parameters:
            key (str): key for which we need the value

        Returns:
            str: value linked to the key, None if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
