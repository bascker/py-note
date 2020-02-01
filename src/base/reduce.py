#!/usr/bin/python
"""
reduce 语法:  reduce(function, list)
引入: from functools import reduce
"""

from functools import reduce

fn_mul = lambda x, y: x * y

def _cal(nums):
    return reduce(fn_mul, nums)


def main():
    nums = [1, 2, 3]
    assert 6 == _cal(nums)


if __name__ == '__main__':
    main()
