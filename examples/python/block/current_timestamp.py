"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              c16433a962c1df96c5885f937ba3e1717ec4c8db
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/current-timestamp.py test ff 02 False False
    Expected Result:        1519711047 (Variable)
    Operation Count:        55
    GAS Consumption:        0.145
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Header import GetTimestamp, GetHash, GetNextConsensus  # All these references are needed


def Main():
    """
    :return: Current block timestamp
    :rtype: int
    """
    current_height = GetHeight()
    current_block = GetHeader(current_height)
    timestamp = current_block.Timestamp
    return timestamp
