"""
Date Created:               2018-03-08
Date Modified:              2018-03-08
Version:                    1
Contract Hash:              1aa965c53c373ef9d3be065bdb36b234cdcab66a
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/add.py test 0202 02 False False 2 5
    Expected Result:        2
    Operation Count:        51
    GAS Consumption:        0.045
"""


def Main(a, b):
    """
    :param a: First input number of concern
    :param b: Second input number of concern
    :type a: int
    :type b: int
    :return: The smallest value of the 2 input numbers
    :rtype: int
    """
    result = min(a, b)
    return result
