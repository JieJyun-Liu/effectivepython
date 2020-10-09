"""
Author: Eleven
Date: 2020/10/09
Description: What’s New In Python 3.9
Ref. https://docs.python.org/3.9/whatsnew/3.9.html
"""

from collections import ChainMap


def PEP584():
    """Add Union Operators To dict
    https://www.python.org/dev/peps/pep-0584/

    """
    d1 = {"str_key": 1}
    d2 = {"str_key": 11, 123: 2}
    # dict(d1, **d2)  # error
    merged = ChainMap(d2, d1)
    print(merged)

    # merge two dicts with str keys
    d3 = {"str_key_2": 2}
    print(dict(d1, **d3))  # ac

    # merge two dicts with "or" operator
    print(d1|d2)
    print(d2|d1)


def PEP448():
    """Additional Unpacking Generalizations
    https://www.python.org/dev/peps/pep-0448/

    """
    return


PEP584()
