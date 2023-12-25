#!/usr/bin/env python3
"""function named index_range that takes two int args page and page_size"""


def index_range(page, page_size):
    """
    function to calculate the start and end index for pagination
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
