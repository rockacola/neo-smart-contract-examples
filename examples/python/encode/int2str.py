"""
Date Created:               2018-03-01
Date Modified:              2018-03-01
Version:                    1
Contract Hash:              f992a80d39be3dbc4ecaeb8efaad4118f5a4bc76
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/int2str.py test 02 07 False False 12
    Expected Result:        12
    Operation Count:        263
    GAS Consumption:        0.192

Example: (return as bytearray)
    Test Invoke:            build /path/to/int2str.py test 02 05 False False 12
    Expected Result:        b'12'
    Operation Count:        263
    GAS Consumption:        0.192
"""


def Main(num):
    """
    :param num: Input number of concern
    :type num: int
    :return: The input number in string data type
    :rtype: str
    """
    result = int2str(num)
    return result


def int2str(num):
    digitTexts = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    firstRun = True

    while num > 0:
        remainder = num % 10
        num = num / 10
        digitText = digitTexts[remainder]

        if firstRun:
            result = digitText
            firstRun = False
        else:
            result = concat(digitText, result)

    return result
