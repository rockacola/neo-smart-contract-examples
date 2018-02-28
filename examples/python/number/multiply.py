"""
Date Created:                   2018-02-28
Date Modified:                  2018-02-28
Version:                        1
Contract Hash:                  a9448a2793dd32c3a453e8a83ebed7e3bb10e15e
Available on NEO TestNet:       False
Available on CoZ TestNet:       False
Available on MainNet:           False
Example Build Test Command:     build /path/to/multiply.py test 0505 02 False False 2 5
Example Import Command:         import contract /path/to/multiply.avm 0505 02 False False
Example Invoke:                 testinvoke a9448a2793dd32c3a453e8a83ebed7e3bb10e15e 2 5
Estimate Operation Count:       49
Estimate GAS Consumption:       0.044
"""


def Main(a, b):
    """
    :param a: First input number of concern
    :param b: Second input number of concern
    :type a: int
    :type b: int
    :return: Multiplication of the 2 input numbers
    :rtype: int
    """
    c = a * b  # It is a good practice to always allocate calculated value to a local variable instead of chaining to return or another function
    return c
