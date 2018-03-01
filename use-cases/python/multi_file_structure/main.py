"""
Date Created:               2018-03-01
Date Modified:              2018-03-01
Version:                    1
Contract Hash:              ee4fc9a20e7b413a9fc830453a8a6a278f7590e5
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
VERSION = 3


def Main(operation: str, args: list) -> bytearray:
    # Purpose of this contract is to demonstrate possible multi file structure. Hence there will be no documentations on its implementations.
    if operation == 'version':
        result = do_version()
        return result
    if operation == 'magic_word':
        result = do_magic_word()
        return result
    if operation == 'add':
        result = do_add(args)
        return result
    Notify(ErrorResponse.UnknownOperation())
    return False


def do_version() -> int:
    version = VERSION
    Notify('version:')
    Notify(version)
    return version


def do_magic_word() -> str:
    result = Config.MagicWord()
    return result


def do_add(args: list) -> int:
    if len(args) > 1:
        n1 = args[0]
        n2 = args[1]
        result = MathHelper.Add(n1, n2)
        return result
    Notify(ErrorResponse.InvalidArgsLength())
    return False
