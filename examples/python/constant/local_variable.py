"""
Date Created:               2018-03-08
Date Modified:              2018-03-08
Version:                    1
Contract Hash:              f8c1e4600b8f9a08b015c7c549f0eeeb1e2d8b61
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/local_variable.py test ff 07 False False
    Expected Result:        magic value
    Operation Count:        23
    GAS Consumption:        0.025
"""


def Main():
    """
    :return: Static string from local variable.
    :rtype: str
    """
    MAGIC = 'magic value'  # Constant declared within scope of a method, only
    return MAGIC
