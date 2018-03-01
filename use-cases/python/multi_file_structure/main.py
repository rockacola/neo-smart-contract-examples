"""
Date Created:               2018-03-01
Date Modified:              2018-03-02
Version:                    4
Contract Hash:              f31fef19465e16caa6e5dc8beab99a6a628e2f72
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/main.py test 0710 05 False False version
    Expected Result:        b'\x02'
    Operation Count:        100
    GAS Consumption:        0.077
"""


from boa.blockchain.vm.Neo.Runtime import Notify
from pkg.helpers.math_helper import MathHelper
from pkg.settings.config import Config
from pkg.settings.responses import ErrorResponse


# Global
VERSION = 4


def Main(operation: str, args: list) -> bytearray:
    # Purpose of this contract is to demonstrate possible multi file structure. Hence there will be no documentations on its implementations.
    """
    Note:
        - Usage of static methods or properties are discouraged, due to unconventional syntax. You'll have better luck to instantiate classes when needed.
    """
    if operation == 'version':
        result = do_version()
        return result
    if operation == 'magic_word':
        result = do_magic_word()
        return result
    if operation == 'add':
        result = do_add(args)
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
