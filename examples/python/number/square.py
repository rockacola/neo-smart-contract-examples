"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              b461026b375e04c5aca7bbf7c335ddec8396e49b
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/square.py test 02 02 False False 7
    Expected Result:        49
    Operation Count:        49
    GAS Consumption:        0.039
"""


def Main(num):
    """
    :param num: First input number of concern
    :type num: int
    :return: Square of the input number
    :rtype: int
    """
    result = num * num  # It is a good practice to always allocate calculated value to a local variable instead of chaining to return or another function
    return result
