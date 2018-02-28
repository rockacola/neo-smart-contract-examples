"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              6c92595b7b346ccee1ef3a08d449d98ad0e1a48a
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/block-timestamp.py test 02 02 False False 1
    Expected Result:        1516013740
    Operation Count:        55
    GAS Consumption:        0.144
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeader
from boa.blockchain.vm.Neo.Header import GetTimestamp, GetHash, GetNextConsensus  # All these references are needed


def Main(height):
    """
    :param height: The input block height
    :type height: int
    :return: Block timestamp of the input block height
    :rtype: int
    """
    header = GetHeader(height)
    timestamp = header.Timestamp
    return timestamp
