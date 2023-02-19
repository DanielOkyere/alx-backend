#!/usr/bin/env python3
""" Simple Helper Function """


def index_range(page: int, page_size: int) -> tuple:
    """ index_range
    Args:
        page(int) : start page number
        page_size(int): range to be printed
    Returns:
        Tuple with start and end value of range
    """
    begin_page = 0
    end_page = 0
    if page > 1:
        begin_page += page
        for i in range(1, page+1):
            end_page = begin_page * page_size
        begin_page = end_page - page_size
    else:
        end_page += page_size
    return (begin_page, end_page)
