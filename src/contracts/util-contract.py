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
VERSION = 9
OWNER = b'\x96P\xac\xd6\xb7S,\xb4\xeaiU\xedK\x0f\xd3\xaa\xa9\xc9Q\x87'
NEO_ASSET_ID = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'
GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'
MAGIC_NUMBER = 42
MAGIC_STRING = 'rainbowsix'

def Main(operation: str, args: list) -> bytearray:
    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(OWNER)
        Log('Check is_owner:')
        Log(is_owner)
        if is_owner:
            return True
        return False

    elif trigger == Application():
        if operation == 'version':
            result = do_version()
            return result
        elif operation == 'is_owner':       # Checking if invoker is the owner of the smart contract
            result = do_is_owner()
            return result
        # Constant
        elif operation == 'magic_number':   # Return stored number constant in the contract
            result = do_magic_number()
            return result
        elif operation == 'magic_string':   # Return stored string constant in the contract
            result = do_magic_string()
            return result
        elif operation == 'neo_id':         # Return stored bytearray constant in the contract
            result = do_neo_id()
            return result
        # Number
        elif operation == 'add':            # Adding 2 numbers together
            result = do_add(args)
            return result
        elif operation == 'multiply':       # Multiply 2 numbers together
            result = do_multiply(args)
            return result
        elif operation == 'square':         # Returns square of a given value
            result = do_square(args)
            return result
        elif operation == 'power':          # Return base to the exponent power. Only support positive integers
            result = do_power(args)
            return result
        elif operation == 'fibonacci':      # Returns Fibonacci value of a given number
            result = do_fibonacci(args)
            return result
        # String
        elif operation == 'char_count':     # Return character count of input string
            result = do_char_count(args)
            return result
        elif operation == 'string_reverse': # Return input string in reverse order
            result = do_string_reverse(args)
            return result
        # Array
        elif operation == 'length':         # Get length of input arguments array
            result = do_length(args)
            return result
        elif operation == 'add_array':      # Adding all numbers in array together
            result = do_add_array(args)
            return result
        # Storage
        elif operation == 'set_storage':    # Update storage of specified key
            result = do_set_storage(args)
            return result
        elif operation == 'get_storage':    # Obtain stored data of specified key
            result = do_get_storage(args)
            return result
        # Block
        elif operation == 'height':         # Get current block height
            result = do_height()
            return result
        elif operation == 'current_timestamp':      # Get timestamp of current block
            result = do_current_timestamp()
            return result
        elif operation == 'get_timestamp':      # Get timestamp of current block
            result = do_get_timestamp(args)
            return result
        elif operation == 'get_merkle':
            result = do_get_merkle(args)
            return result
        elif operation == 'get_block_hash':
            result = do_get_block_hash(args)
            return result
        elif operation == 'get_consensus':
            result = do_get_consensus(args)
            return result
        elif operation == 'get_next_consensus':
            result = do_get_next_consensus(args)
            return result
        # Account
        elif operation == 'my_address':     # Get invoker's wallet address in bytearray
            result = do_my_address()
            return result
        elif operation == 'target_address': # Get the target address in bytearray
            result = do_target_address()
            return result
        elif operation == 'is_address':     # Check if invoker's address matches the specified address
            result = do_is_address(args)
            return result
        elif operation == 'is_witness_address':      # Check if invoker's address matches the specified address
            result = do_is_witness_address(args)
            return result

        Log('unknown operation')
        return False

    Log('invalid request')
    return False


def do_version() -> int:
    version = VERSION
    Notify(version)
    return version


def do_is_owner() -> bool:
    return CheckWitness(OWNER)


# -- Contant


def do_magic_number():
    result = MAGIC_NUMBER
    return result


def do_magic_string():
    result = MAGIC_STRING
    return result


def do_neo_id():
    result = NEO_ASSET_ID
    return result


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


def do_char_count(args: list) -> int:
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


def do_length(args: list) -> int:
    result = len(args)
    return result


def do_add_array(args: list) -> int:
    if len(args) > 1:
        result = 0
        for val in args:
            result = result + val
        return result
    Notify('invalid argument length')
    return False


# -- Storage


def do_set_storage(args: list) -> bool:
    if len(args) > 1:
        key = args[0]
        data = args[1]
        context = GetContext()
        result = set_storage(context, key, data)
        return result
    Notify('invalid argument length')
    return False


def do_get_storage(args: list) -> bytearray:
    if len(args) > 0:
        key = args[0]
        context = GetContext()
        result = get_storage(context, key)
        return result
    Notify('invalid argument length')
    return False


# -- Block


def do_height() -> int:
    Log('do_height triggered.')
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


def do_get_merkle(args: list) -> bytearray:
    Log('do_get_merkle triggered.')
    if len(args) > 0:
        height = args[0]
        Log('height:')
        Log(height)
        header = GetHeader(height)
        version = GetVersion(header)
        Log('version:')
        Log(version)
        merkle = GetMerkleRoot(header)
        Log('merkle:')
        Log(merkle)
        return merkle
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


# -- Account


def do_my_address() -> bytearray:
    Log('do_my_address triggered.')
    sender_address = get_my_address()
    Log('sender_address:')
    Log(sender_address)
    return sender_address


def do_target_address() -> bytearray:
    Log('do_target_address triggered.')
    receiver_address = get_target_address()
    Log('receiver_address:')
    Log(receiver_address)
    return receiver_address


def do_is_address(args: list) -> bool:
    if len(args) > 0:
        Log('do_is_address triggered.')
        target_address = args[0]
        Log('target_address:')
        Log(target_address)
        target_address_length = len(target_address)
        Log('target_address_length:')
        Log(target_address_length)
        sender_address = get_my_address()
        Log('sender_address:')
        Log(sender_address)
        result = (target_address == sender_address)
        Log('result:')
        Log(result)
        return result
    Notify('invalid argument length')
    return False


def do_is_witness_address(args: list) -> bool:
    if len(args) > 0:
        Log('do_is_witness_address triggered.')
        target_address = args[0]
        Log('target_address:')
        Log(target_address)
        is_match = CheckWitness(target_address)
        Log('is_match:')
        Log(is_match)
        return is_match
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


def get_my_address() -> bytearray:
    Log('get_my_address triggered.')
    tx = GetScriptContainer()
    Log('tx:')
    Log(tx)
    references = tx.References
    Log('references:')
    Log(references)
    reference = references[0]
    Log('reference:')
    Log(reference)
    sender_address = reference.ScriptHash
    Log('sender_address:')
    Log(sender_address)
    return sender_address


def get_target_address() -> bytearray:
    Log('get_target_address triggered.')
    receiver_address = GetExecutingScriptHash()
    Log('receiver_address:')
    Log(receiver_address)
    return receiver_address


def set_storage(context, key: str, value: bytearray) -> bool:
    Put(context, key, value)
    return True


def get_storage(context, key: str) -> bytearray:
    value = Get(context, key)
    return value
