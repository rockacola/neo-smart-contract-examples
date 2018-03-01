"""
Date Created:               2018-02-27
Date Modified:              2018-02-27
Version:                    1
Contract Hash:              b6906e1806a9d9c49de12a192bcb55b77ecae840
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/is-owner.py test ff 01 False False
    Expected Result:        False
    Operation Count:        45
    GAS Consumption:        0.239
"""


from boa.blockchain.vm.Neo.Runtime import CheckWitness


OWNER = b'\x96P\xac\xd6\xb7S,\xb4\xeaiU\xedK\x0f\xd3\xaa\xa9\xc9Q\x87'


def Main(arr):
    """
    :return: Whether the invoker is defined as owner of this contract
    :rtype: bool
    """
    is_owner = CheckWitness(OWNER)  # Built-in CheckWitness() function able to determine whether the contract invoker matches to the provided address in byte array
    return is_owner
