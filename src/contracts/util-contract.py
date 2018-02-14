"""
TODO:
- Get current transaction hash
- Get invoker's address
- Get attached asset details
- Get string name of the type of input argument
- Concate 2 values of any datatype together
- Concate n strings together
- String replace
- String indexOf
- Set key-value into context (test non-ASCII characters, and crazy length)
- Get key-value from context
- Check if a key exists in context
- Array storage example (pop, push, fetch, count)
- Get block timestamp

Test Command:
    build ./demo/contracts/util-contract.py test 0710 05 True False version
    build ./demo/contracts/util-contract.py test 0710 05 True False my_address --attach-gas=1
    build ./demo/contracts/util-contract.py test 0710 05 True False is_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'] --attach-gas=1
    build ./demo/contracts/util-contract.py test 0710 05 True False is_witness_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
    build ./demo/contracts/util-contract.py test 0710 05 True False char_count ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']

Import Command:
    import contract ./demo/contracts/util-contract.avm 0710 05 True False

Example Invocation:
    testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc version
    testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc my_address [] --attach-gas=1 # Output: b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'
    testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc is_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'] --attach-gas=1
"""
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.code.builtins import concat, list, range, take, substr


# Global
VERSION = 7
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'  # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
# NEO_ASSET_ID = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'
# GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'


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
        # Block
        elif operation == 'height':         # Get current block height
            result = do_height()
            return result
        # Account
        elif operation == 'my_address':     # Get invoker's wallet address in bytearray
            result = do_my_address()
            return result
        elif operation == 'is_address':      # Check if invoker's address matches the specified address
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


# -- Block


def do_height() -> int:
    current_height = GetHeight()
    return current_height


# -- Account


def do_my_address() -> bytearray:
    Log('do_my_address triggered.')
    sender_addr = get_my_address()
    Log('sender_addr:')
    Log(sender_addr)
    return sender_addr


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
    # Log('get_my_address triggered.')
    tx = GetScriptContainer()
    # Log('tx:')
    # Log(tx)
    # TODO: tx None check
    references = tx.References
    # Log('references:')
    # Log(references)
    # TODO: references None and length check
    # receiver_addr = GetExecutingScriptHash()
    # Log('receiver_addr:')
    # Log(receiver_addr)
    reference = references[0]
    # Log('reference:')
    # Log(reference)
    sender_addr = reference.ScriptHash
    # Log('sender_addr:')
    # Log(sender_addr)
    return sender_addr
