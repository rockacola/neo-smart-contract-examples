"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              18f6498f257ffd1e62593a5ec1407486ad1b923f
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example: (return as bytearray)
    Test Invoke:            build /path/to/block-hash.py test 02 05 False False 1
    Expected Result:        bytearray(b'\xbf\xa9\xdd\x88\xd2\xde\xb8\x15\x8cdl\x15\x8f\x13\x97%\xd1P\xe6y\x12!\t\x13\x8a\x8a\xd7s;ix\x8b')
    Operation Count:        53
    GAS Consumption:        0.144

Example: (return as integer)
    Test Invoke:            build /path/to/block-hash.py test 02 02 False False 1
    Expected Result:        -52707855350265912913046510941463189951377470409872379814054685480828117603905
    Operation Count:        53
    GAS Consumption:        0.144
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeader
from boa.blockchain.vm.Neo.Header import GetHash, GetNextConsensus  # All these references are needed


def Main(height):
    """
    :param height: The input block height
    :type height: int
    :return: Block hash of the input block height
    :rtype: bytearray
    """
    header = GetHeader(height)
    hash_val = GetHash(header)
    return hash_val
