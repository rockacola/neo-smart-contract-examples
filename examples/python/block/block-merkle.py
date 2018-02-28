"""
Date Created:               2018-02-28
Date Modified:              2018-02-28
Version:                    1
Contract Hash:              bebbd908e9f724525f4a9058ba0bc9d4d858b074
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example: (return as bytearray)
    Test Invoke:            build /path/to/block-merkle.py test 02 05 False False 1
    Expected Result:        bytearray(b'_\xc3 \xe8\xcc\xbf50_\xdb\x93\xa3\x01\x87Y\x88\xba&\x9e\x17\xad\x80\xc9\xfa\xd0\xf6\xaf\xc6\x7fH\x99$')
    Operation Count:        53
    GAS Consumption:        0.144

Example: (return as integer)
    Test Invoke:            build /path/to/block-merkle.py test 02 02 False False 1
    Expected Result:        16554090520483099625892320194318787314436399351031916891542174392554652484447
    Operation Count:        53
    GAS Consumption:        0.144

Note:
    - When returning value in integer, it is not necessary a positive value. For example: height 2000 can returns -10598162010060948421498424940748046520573587672645442717203918160812353968013.
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeader
from boa.blockchain.vm.Neo.Header import GetMerkleRoot, GetHash, GetNextConsensus  # All these references are needed


def Main(height):
    """
    :param height: The input block height
    :type height: int
    :return: Block merkle value of the input block height
    :rtype: bytearray
    """
    header = GetHeader(height)
    merkle = GetMerkleRoot(header)
    return merkle
