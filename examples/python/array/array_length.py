"""
Date Created:               2018-02-27
Date Modified:              2018-02-27
Version:                    1
Contract Hash:              0a8b34b4097f0a472d5a31726d70ff807d37490d
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/array-length.py test 10 02 False False [True,'two',3]
    Expected Result:        3
    Operation Count:        41
    GAS Consumption:        0.035

Note:
    - This example has the same implementation and hence generates the same contract hash as "string/character-count.py"
    - Following input parameters will results in incorrect result:
        - [True,'two',3,[]]
"""


def Main(arr):
    """
    :param arr: Input array of concern
    :type arr: list
    :return: Size of the input array
    :rtype: int
    """
    result = len(arr)  # Obtain array length by using built in len() function
    return result
