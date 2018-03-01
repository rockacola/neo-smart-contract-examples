"""
Date Created:               2018-03-01
Date Modified:              2018-03-01
Version:                    1
Contract Hash:              TBA
Available on NEO TestNet:   False
Available on CoZ TestNet:   False
Available on MainNet:       False

Example:
    Test Invoke:            build /path/to/main.py test 0710 05 False False version
    Expected Result:        TBA
    Operation Count:        TBA
    GAS Consumption:        TBA
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
from pkg.helpers.math_helper import MathHelper


# Global
VERSION = 1


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
    Log('unknown operation')
    return False


def do_version() -> int:
    version = VERSION
    Notify('version:')
    Notify(version)
    return version


def do_magic_word() -> str:
    result = 'magic!'
    return result


def do_add(args: list) -> int:
    if len(args) > 1:
        n1 = args[0]
        n2 = args[1]
        # helper = MathHelper()
        # result = helper.add(n1, n2)
        # result = n1 + n2
        result = MathHelper.Add(n1, n2)
        return result
    Notify('invalid argument length')
    return False
