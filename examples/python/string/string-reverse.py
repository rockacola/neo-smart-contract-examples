"""
Date Created:               2018-02-27
Date Modified:              2018-02-27
Version:                    1
Contract Hash:              3eb1b3eef48650101b56b4048cbfe269debf9ce0
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/string-reverse.py test 07 07 False False lorem
    Expected Result:        merol
    Operation Count:        397
    GAS Consumption:        0.300
"""


def Main(text):
    """
    :param text: Input string of concern
    :type text: str
    :return: The reversed string
    :rtype: str
    """
    result = ''
    length = len(text)
    index = 0
    while index < length:
        current_char = substr(text, index, 1)
        result = concat(current_char, result)
        index = index + 1
    return result
