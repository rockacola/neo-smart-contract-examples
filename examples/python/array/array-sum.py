"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              b94ef8e59d227dac1ea9b66d61cb6d35b90c9e46
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/array-sum.py test 10 02 False False [2,4,6]
    Expected Result:        12
    Operation Count:        264
    GAS Consumption:        0.203

Note:
    - It is assumed that all items are integer, no validation process is in place.
"""


def Main(arr):
    """
    :param arr: Input array of concern
    :type arr: list
    :return: Sum of all values in array
    :rtype: int
    """
    result = 0
    for val in arr:  # Using for ... in syntax
        result = result + val
    return result
