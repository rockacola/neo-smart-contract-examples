"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              5302d1880fc2de0cd968a178c7495651635a228e
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example: (return as bytearray)
    Test Invoke:            build /path/to/next-consensus.py test 02 05 False False 1
    Expected Result:        bytearray(b'\xbeH\xd3\xa3\xf5\xd1\x00\x13\xab\x9f\xfe\xe4\x89p`xqO\x1e\xa2')
    Operation Count:        53
    GAS Consumption:        0.144

Example: (return as integer)
    Test Invoke:            build /path/to/next-consensus.py test 02 02 False False 1
    Expected Result:        -535969189618980822910524473263859743778491119426
    Operation Count:        53
    GAS Consumption:        0.144
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeader
from boa.blockchain.vm.Neo.Header import GetHash, GetNextConsensus  # All these references are needed


def Main(height):
    """
    :param height: The input block height
    :type height: int
    :return: Next consensus data of the input block height
    :rtype: bytearray
    """
    header = GetHeader(height)
    next_consensus = header.NextConsensus
    return next_consensus
