#!/usr/bin/env python3
""" Simple Helper Function """
import csv
import math
from typing import List, Dict


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


class Server:
    """ Server class to paginate a database of popular baby
    names
    """
    DATA_FILE = "./Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page: asserts if page and page_size are int
        Args:
            page: int
            page_size: int
        Returns:
            If indexes are correct paginates the dataset
            correctly and return appropriate page
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page >= 1
        assert page_size >= 1
        data_range = index_range(page, page_size)
        if page > len(self.dataset()):
            return []
        else:
            return self.dataset()[data_range[0]:data_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get_hyper: asserts if page and page_size are int
        Args:
            page (int) page number
            page_size (int) size of the page
        Returns:
            Dictionary of values :
                page_size: length of returned dataset page
                page: the current page number
                data: the dataset page equivalent
                    to return from previous
                next_page: number of the next page,
                    None if no next page
                prev_page: number of the previous page,
                    None if no previous page
                total_pages: the total number of pages
                   in the dataset as an integer
        """
        data_range = index_range(page, page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if data_range[1] < len(self.__dataset) else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': page - 1 if data_range[0] < 0 else None,
            'total_pages': math.ceil(len(self.__dataset)/page_size)
        }
