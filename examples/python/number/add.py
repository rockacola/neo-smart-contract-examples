"""
Date Created:               2018-02-27
Date Modified:              2018-02-27
Version:                    1
Contract Hash:              28dfdb9d1d0fa0b86804e4a4e0f0c42484f32792
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/add.py test 0202 02 False False 2 5
    Expected Result:        7
    Operation Count:        11
    GAS Consumption:        0.016
"""


def Main(a, b):
    """
    :param a: First input number of concern
    :param b: Second input number of concern
    :type a: int
    :type b: int
    :return: Sum of the 2 input numbers
    :rtype: int
    """
    c = a + b  # It is a good practice to always allocate calculated value to a local variable instead of chaining to return or another function
    return c
