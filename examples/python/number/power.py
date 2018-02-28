"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              b6c8ab8ca45c240d7b4a965ecaa5d85eb1439aae
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/power.py test 0202 02 False False 2 8
    Expected Result:        256
    Operation Count:        421
    GAS Consumption:        0.330
"""


def Main(base, exp):
    """
    :param base: The base number
    :type base: int
    :param exp: The exponent used to raise the base
    :type exp: int
    :return: A number representing the given base taken to the power of the given exponent
    :rtype: int
    """
    result = 1
    index = 0
    while index < exp:
        result = result * base
        index = index + 1
    return result
