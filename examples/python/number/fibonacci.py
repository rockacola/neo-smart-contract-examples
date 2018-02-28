"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              3147293325d465b73a692112f54295718fabd35f
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/fibonacci.py test 02 02 False False 3
    Expected Result:        2
    Operation Count:        203
    GAS Consumption:        0.156

Example:
    Test Invoke:            build /path/to/fibonacci.py test 02 02 False False 11
    Expected Result:        89
    Operation Count:        12293
    GAS Consumption:        9.006

Example:
    Test Invoke:            build /path/to/fibonacci.py test 02 02 False False 15
    Expected Result:        610
    Operation Count:        84683
    GAS Consumption:        61.996
"""


def Main(num):
    """
    :param num: First input number of concern
    :type num: int
    :return: The fibonacci value of the input number
    :rtype: int
    """
    result = get_fibonacci(num)  # It is a good practice to always allocate calculated value to a local variable instead of chaining to return or another function
    return result


def get_fibonacci(n):
    """
    A self-recursive function to obtain the final fibonacci result.

    :type n: int
    :rtype: int
    """
    if n == 1 or n == 2:
        return 1
    n1 = n - 1
    n2 = n - 2
    fibr1 = get_fibonacci(n1)
    fibr2 = get_fibonacci(n2)
    res = fibr1 + fibr2
    return res
