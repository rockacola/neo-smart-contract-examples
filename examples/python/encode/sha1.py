"""
Date Created:               2018-03-08
Date Modified:              2018-03-08
Version:                    1
Contract Hash:              53c993a91b9c3f7d4bd6bdac8999b90a26249430
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/sha1.py test 07 05 False False lorem
    Expected Result:        b'\xb5\x8e\x92\xff\xf5$fE\xf7r\xbf\xe7\xa6\x02r\xf3V\xc0\x15\x1a'
    Operation Count:        37
    GAS Consumption:        0.044
"""


# from boa.builtins import sha1
from boa.code.builtins import sha1


def Main(text):
    """
    :param num: Input string of concern
    :type num: str
    :return: SHA1 hash value of the input string
    :rtype: bytearray
    """
    result = sha1(text)
    return result
