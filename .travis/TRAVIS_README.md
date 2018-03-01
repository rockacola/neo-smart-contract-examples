# Travis README

## Setup

### From `lint` workstation

* Start local docker: `docker start neo-privnet-with-gas`
* Set to project root: `cd /Users/lint/ProjectGit/rockacola/neo-python`
* Check dependencies: `pip3 install -r requirements.txt`
* Start in PrivNet: `python3 prompt.py -p`
* Enable smart contract events: `config sc-events on`
* Open wallet: `open wallet ./demo/wallets/neo-privnet.wallet`
* Rebuild wallet: `wallet rebuild`

---

## Developer Notes

### To Do

#### High Priority

* Establish communication to seek for C# dev and Chinese translators.
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/RangeTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/OpCallTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/BinopTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/SliceTest.py
  * Is it just for bytearray? can it be applied to string or array?
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/blockchain/AccountTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/blockchain/AppCallTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/blockchain/DynamicAppCallTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/blockchain/TransactionTypeTest.py
* Migrate https://github.com/CityOfZion/neo-boa/blob/master/boa_test/example/blockchain/TriggerTypeTest.py

#### Medium Priority

* Deploy multiple contracts to NEO TestNet

#### Low Priority

* Regression test again NEO TestNet via `neon-js`.

---

## References

TBA
