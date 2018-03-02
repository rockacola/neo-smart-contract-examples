from boa.blockchain.vm.Neo.Runtime import Notify
from pkg.models.storage import Storage


class Counter():
    KEY = 'counter'

    def get(self) -> int:
        Notify('Counter.get triggered.')
        storage = Storage()
        result = storage.get(self.KEY)
        if (result == None):
            return 0
        else:
            return result
        return result

    def up(self) -> None:
        Notify('Counter.up triggered.')
        current_count = self.get()
        new_count = current_count + 1
        storage = Storage()
        storage.put(self.KEY, new_count)
        return None

    def down(self) -> None:
        Notify('Counter.down triggered.')
        current_count = self.get()
        new_count = current_count - 1
        storage = Storage()
        storage.put(self.KEY, new_count)
        return None
