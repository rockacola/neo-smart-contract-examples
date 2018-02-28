"""
Date Created:                   2018-02-27
Date Modified:                  2018-02-27
Version:                        1
Contract Hash:                  28dfdb9d1d0fa0b86804e4a4e0f0c42484f32792
Available on NEO TestNet:       False
Available on CoZ TestNet:       False
Available on MainNet:           False
Example Build Test Command:     build /path/to/add.py test 0505 02 False False 2 5
Example Import Command:         import contract /path/to/add.avm 0505 02 False False
Example Invoke:                 testinvoke 28dfdb9d1d0fa0b86804e4a4e0f0c42484f32792 2 5
Estimate Operation Count:       11
Estimate GAS Consumption:       0.016
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
