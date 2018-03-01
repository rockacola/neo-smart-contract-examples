from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

class Storage():
    context = GetContext()

    def get(self, key: str) -> bytearray:
        return Get(self.context, key)

    def put(self, key: str, value: bytearray) -> None:
        Put(self.context, key, value)

    def delete(self, key: str) -> None:
        Delete(self.context, key)
