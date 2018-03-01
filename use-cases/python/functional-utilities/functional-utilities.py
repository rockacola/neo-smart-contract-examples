"""
Date Created:                   2018-02-05
Date Modified:                  2018-03-01
Version:                        11
Contract Hash:                  830629f06d252ff7a3b38016df5e88426f596000
Available on NEO TestNet:       False
Available on CoZ TestNet:       False
Available on MainNet:           False

Example:
    Test Invoke:            build /path/to/functional-utilities.py test 0710 05 False False version
    Expected Result:        b'\n'
    Operation Count:        100
    GAS Consumption:        0.077
"""


from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Header import GetMerkleRoot, GetTimestamp, GetHash, GetVersion, GetConsensusData, GetNextConsensus
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.code.builtins import concat, list, range, take, substr


# Global
VERSION = 10


def Main(operation: str, args: list) -> bytearray:
    """
    :param opeartion: Name of the operation to execute
    :param args: List of supplied arguments. Cannot be null
    :type opeartion: str
    :type args: list
    :return: Response value depends on selected operation
    :rtype: bytearray
    """
    if operation == 'version':
        result = do_version()               # Get version number of this contract
        return result
    # Number
    elif operation == 'add':                # Adding 2 numbers together
        result = do_add(args)
        return result
    elif operation == 'multiply':           # Multiply 2 numbers together
        result = do_multiply(args)
        return result
    elif operation == 'square':             # Returns square of a given value
        result = do_square(args)
        return result
    elif operation == 'power':              # Return base to the exponent power. Only support positive integers
        result = do_power(args)
        return result
    elif operation == 'fibonacci':          # Returns Fibonacci value of a given number
        result = do_fibonacci(args)
        return result
    # String
    elif operation == 'character_count':    # Return character count of input string
        result = do_character_count(args)
        return result
    elif operation == 'string_reverse':     # Return input string in reverse order
        result = do_string_reverse(args)
        return result
    # Array
    elif operation == 'array_length':       # Get length of input arguments array
        result = do_array_length(args)
        return result
    elif operation == 'array_sum':          # Adding all numbers in array together
        result = do_array_sum(args)
        return result
    # Block
    elif operation == 'current_height':     # Get current block height
        result = do_current_height()
        return result
    elif operation == 'current_timestamp':  # Get timestamp of current block
        result = do_current_timestamp()
        return result
    elif operation == 'get_timestamp':      # Get timestamp of specified block height
        result = do_get_timestamp(args)
        return result
    elif operation == 'get_merkle_root':    # Get merkle root of specified block height
        result = do_get_merkle_root(args)
        return result
    elif operation == 'get_block_hash':     # Get hash of specified block height
        result = do_get_block_hash(args)
        return result
    elif operation == 'get_consensus':      # Get consensus value of specified block height
        result = do_get_consensus(args)
        return result
    elif operation == 'get_next_consensus': # Get next consensus value of specified block height
        result = do_get_next_consensus(args)
        return result

    Log('unknown operation')
    return False


def do_version() -> int:
    version = VERSION
    Notify('version:')
    Notify(version)
    return version


# -- Number


def do_add(args: list) -> int:
    if len(args) > 1:
        n1 = args[0]
        n2 = args[1]
        result = n1 + n2
        return result
    Notify('invalid argument length')
    return False


def do_multiply(args: list) -> int:
    if len(args) > 1:
        n1 = args[0]
        n2 = args[1]
        result = n1 * n2
        return result
    Notify('invalid argument length')
    return False


def do_square(args: list) -> int:
    if len(args) > 0:
        val = args[0]
        result = val * val
        return result
    Notify('invalid argument length')
    return False


def do_power(args: list) -> int:
    if len(args) > 1:
        input_base = args[0]
        input_exp = args[1]
        result = 1
        index = 0
        while index < input_exp:
            result = result * input_base
            index = index + 1
        return result
    Notify('invalid argument length')
    return False


def do_fibonacci(args: list) -> int:
    if len(args) > 0:
        val = args[0]
        result = get_fibonacci(val)
        return result
    Notify('invalid argument length')
    return False


# -- String


def do_character_count(args: list) -> int:
    if len(args) > 0:
        val = args[0]
        result = len(val)
        return result
    Notify('invalid argument length')
    return False


def do_string_reverse(args: list) -> str:
    if len(args) > 0:
        result = ''
        val = args[0]
        length = len(val)
        index = 0
        while index < length:
            current_char = substr(val, index, 1)
            result = concat(current_char, result)
            index = index + 1
        return result
    Notify('invalid argument length')
    return False


# -- Array


def do_array_length(args: list) -> int:
    result = len(args)
    return result


def do_array_sum(args: list) -> int:
    if len(args) > 1:
        result = 0
        for val in args:
            result = result + val
        return result
    Notify('invalid argument length')
    return False


# -- Block


def do_current_height() -> int:
    Log('do_current_height triggered.')
    current_height = GetHeight()
    Log('current_height:')
    Log(current_height)
    return current_height


def do_current_timestamp() -> bytearray:
    Log('do_current_timestamp triggered.')
    current_height = GetHeight()
    Log('current_height:')
    Log(current_height)
    current_block = GetHeader(current_height)
    # Log('current_block:')
    # Log(current_block)
    timestamp = current_block.Timestamp
    Log('timestamp:')
    Log(timestamp)  # Example b'\xc1\xc7|Z'
    return timestamp


def do_get_timestamp(args: list) -> bytearray:
    Log('do_get_timestamp triggered.')
    if len(args) > 0:
        height = args[0]
        Log('height:')
        Log(height)
        header = GetHeader(height)
        timestamp = header.Timestamp
        Log('timestamp:')
        Log(timestamp)
        return timestamp
    Notify('invalid argument length')
    return False


def do_get_merkle_root(args: list) -> bytearray:
    Log('do_get_merkle_root triggered.')
    if len(args) > 0:
        height = args[0]
        Log('height:')
        Log(height)
        header = GetHeader(height)
        version = GetVersion(header)
        Log('version:')
        Log(version)
        merkle_root = GetMerkleRoot(header)
        Log('merkle_root:')
        Log(merkle_root)
        return merkle_root
    Notify('invalid argument length')
    return False


def do_get_block_hash(args: list) -> bytearray:
    Log('do_get_block_hash triggered.')
    if len(args) > 0:
        height = args[0]
        Log('height:')
        Log(height)
        header = GetHeader(height)
        # version = GetVersion(header)
        hash_val = GetHash(header)
        Log('hash_val:')
        Log(hash_val)
        return hash_val
    Notify('invalid argument length')
    return False


def do_get_consensus(args: list) -> bytearray:
    Log('do_get_consensus triggered.')
    if len(args) > 0:
        height = args[0]
        Log('height:')
        Log(height)
        header = GetHeader(height)
        consensus = header.ConsensusData
        Log('consensus:')
        Log(consensus)
        return consensus
    Notify('invalid argument length')
    return False


def do_get_next_consensus(args: list) -> bytearray:
    Log('do_get_next_consensus triggered.')
    if len(args) > 0:
        height = args[0]
        Log('height:')
        Log(height)
        header = GetHeader(height)
        next_consensus = header.NextConsensus
        Log('next_consensus:')
        Log(next_consensus)
        return next_consensus
    Notify('invalid argument length')
    return False


# -- Private methods


def get_fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    n1 = n - 1
    n2 = n - 2
    fibr1 = get_fibonacci(n1)
    fibr2 = get_fibonacci(n2)
    res = fibr1 + fibr2
    return res
