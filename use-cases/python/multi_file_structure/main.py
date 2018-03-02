"""
Date Created:               2018-03-01
Date Modified:              2018-03-02
Version:                    5
Contract Hash:              1d9508f770dc21bb0f391e96c3b133a6b577ada3
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/main.py test 0710 05 True False version
    Expected Result:        b'\x02'
    Operation Count:        100
    GAS Consumption:        0.077
"""


from boa.blockchain.vm.Neo.Runtime import Notify
from pkg.helpers.math_helper import MathHelper
from pkg.settings.config import Config
from pkg.settings.responses import ErrorResponse
from pkg.models.storage import Storage
from pkg.models.counter import Counter


# Global
VERSION = 5


def Main(operation: str, args: list) -> bytearray:
    # Purpose of this contract is to demonstrate possible multi file structure. Hence there will be no documentations on its implementations.
    """
    Note:
        - Usage of static methods or properties are discouraged, due to unconventional syntax. You'll have better luck to instantiate classes when needed.
    """
    if operation == 'version':
        result = do_version()
        return result
    elif operation == 'magic_word':
        result = do_magic_word()
        return result
    elif operation == 'add':
        result = do_add(args)
        return result
    elif operation == 'get_count':
        result = do_get_count()
        return result
    elif operation == 'count_up':
        result = do_count_up()
        return result
    elif operation == 'count_down':
        result = do_count_down()
        return result
    err = ErrorResponse()
    Notify(err.unknown_operation)
    return False


def do_version() -> bytearray:
    version = VERSION
    Notify('version:')
    Notify(version)
    return version


def do_magic_word() -> bytearray:
    config = Config()
    result = config.magic_word
    return result


def do_add(args: list) -> bytearray:
    if len(args) > 1:
        n1 = args[0]
        n2 = args[1]
        result = MathHelper.Add(n1, n2)
        return result
    err = ErrorResponse()
    return err.invalid_args_length


def do_get_count() -> bytearray:
    counter = Counter()
    result = counter.get()
    return result


def do_count_up() -> bytearray:
    counter = Counter()
    result = counter.up()
    return True


def do_count_down() -> bytearray:
    counter = Counter()
    result = counter.down()
    return True
