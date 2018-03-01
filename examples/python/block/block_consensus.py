"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              6f873e1c9b6f306fb41f9a9a81ce32df726a1fb4
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example: (return as bytearray)
    Test Invoke:            build /path/to/block-consensus.py test 02 05 False False 1
    Expected Result:        b'd<\t6\xaf\x9c\xdb\xb4\x00'
    Operation Count:        53
    GAS Consumption:        0.144

Example: (return as integer)
    Test Invoke:            build /path/to/block-consensus.py test 02 02 False False 1
    Expected Result:        13032182223066446948
    Operation Count:        53
    GAS Consumption:        0.144
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeader
from boa.blockchain.vm.Neo.Header import GetHash, GetConsensusData, GetNextConsensus  # All these references are needed


def Main(height):
    """
    :param height: The input block height
    :type height: int
    :return: Block consensus data of the input block height
    :rtype: bytearray
    """
    header = GetHeader(height)
    consensus = header.ConsensusData
    return consensus
