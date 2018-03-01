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

## Contacts Executions

### From `lint` workstation

#### Constant

##### 42

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/forty_two.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/forty_two.avm ff 02 False False
```

#### Number

##### Add

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.py test 0202 02 False False 2 5
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.avm 0202 02 False False
```

##### Multiply

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/multiply.py test 0202 02 False False 2 5
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/multiply.avm 0202 02 False False
```

##### Square

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/square.py test 02 02 False False 7
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/square.avm 02 02 False False
```

##### Power

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/power.py test 0202 02 False False 2 8
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/power.avm 0202 02 False False
```

##### Fibonnaci

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/fibonacci.py test 02 02 False False 3
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/fibonacci.avm 02 02 False False
```

#### String

##### Character Count

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/character_count.py test 07 02 False False lorem
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/character_count.avm 07 02 False False
```

##### String Reverse

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/string_reverse.py test 07 07 False False lorem
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/string_reverse.avm 07 07 False False
```

#### Array

##### Array Length

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array_length.py test 10 02 False False [True,'two',3]
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array_length.avm 10 02 False False
```

##### Array Sum

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array_sum.py test 10 02 False False [2,4,6]
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array_sum.avm 10 02 False False
```

#### Encode

##### Int to Str

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/encode/int2str.py test 02 05 False False 12
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/encode/int2str.avm 02 05 False False
```

#### Block

##### Current Height

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current_height.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current_height.avm ff 02 False False
```

##### Current Timestamp

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current_timestamp.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current_timestamp.avm ff 02 False False
```


##### Block Timestamp

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_timestamp.py test 02 02 False False 1
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_timestamp.avm 02 02 False False
```

##### Block Merkle Root

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_merkle-root.py test 02 02 False False 1
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_merkle-root.avm 02 02 False False
```

##### Block Hash

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_hash.py test 02 02 False False 1
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_hash.avm 02 02 False False
```

##### Block Consensus

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_consensus.py test 02 02 False False 1
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block_consensus.avm 02 02 False False
```

##### Next Consensus

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/next_consensus.py test 02 02 False False 1
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/next_consensus.avm 02 02 False False
```

#### Account

##### Is Owner

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is_owner.py test ff 01 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is_owner.avm ff 01 False False
```

#### Use Cases

##### Functional Utilities

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False version
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False add [2,5]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False multiply [7,6]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False square [6]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False power [2,8]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False fibonacci [7]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False character_count ['lorem']
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False string_reverse ['lorem']
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False array_length [1,2,3]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False array_sum [1,2,3]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False current_height []
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False current_timestamp []
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_timestamp [1]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_merkle_root [1]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_block_hash [1]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_consensus [1]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_next_consensus [1]

import contract /lint/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.avm 0710 05 False False
```

##### Multi File Setup

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/multi_file_structure/main.py test 0710 05 False False version
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/multi_file_structure/main.py test 0710 05 False False add [2,4]
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/multi_file_structure/main.py test 0710 05 False False magic_word
```








---








### From `travis` workstation

#### Number

##### Add

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.py test 0505 02 False False 2 5
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.avm 0505 02 False False
```

#### Block

##### Current Height

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current_height.py test ff 02 False False
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current_height.avm ff 02 False False
```

#### Account

##### Is Owner

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is_owner.py test ff 01 False False
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is_owner.avm ff 01 False False
```

#### Use Cases

##### Functional Utilities

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False version
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False add [2,5]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False multiply [7,6]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False square [6]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False power [2,8]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False fibonacci [7]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False character_count ['lorem']
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False string_reverse ['lorem']
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False array_length [1,2,3]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False array_sum [1,2,3]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False current_height []
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False current_timestamp []
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_timestamp [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_merkle_root [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_block_hash [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_consensus [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.py test 0710 05 False False get_next_consensus [1]

import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional_utilities/functional_utilities.avm 0710 05 False False
```


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
