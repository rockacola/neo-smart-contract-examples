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
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/forty-two.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/forty-two.avm ff 02 False False
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
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/character-count.py test 07 02 False False lorem
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/character-count.avm 07 02 False False
```

##### String Reverse

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/string-reverse.py test 07 07 False False lorem
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/string-reverse.avm 07 07 False False
```

#### Array

##### Array Length

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array-length.py test 10 02 False False [True,'two',3]
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array-length.avm 10 02 False False
```

##### Array Sum

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array-sum.py test 10 02 False False [2,4,6]
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array-sum.avm 10 02 False False
```

#### Block

##### Current Height

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-height.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-height.avm ff 02 False False
```

##### Current Timestamp

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-timestamp.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-timestamp.avm ff 02 False False
```


##### Block Timestamp

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block-timestamp.py test 02 02 False False 1
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/block-timestamp.avm 02 02 False False
```

#### Account

##### Is Owner

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is-owner.py test ff 01 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is-owner.avm ff 01 False False
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
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-height.py test ff 02 False False
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-height.avm ff 02 False False
```

#### Account

##### Is Owner

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is-owner.py test ff 01 False False
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is-owner.avm ff 01 False False
```

#### Use Cases

##### Functional Utilities

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False version
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False add [2,5]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False multiply [7,6]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False square [6]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False power [2,8]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False fibonacci [7]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False character_count ['lorem']
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False string_reverse ['lorem']
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False array_length [1,2,3]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False array_sum [1,2,3]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False current_height []
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False current_timestamp []
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False get_timestamp [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False get_merkle [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False get_block_hash [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False get_consensus [1]
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.py test 0710 05 False False get_next_consensus [1]

import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/use-cases/python/functional-utilities/functional-utilities.avm 0710 05 False False
```


---

## Developer Notes

### To Do

#### High Priority

* Add examples by split up `UtilContract`.
* Once done above, sync to `master`.
* Establish communication to seek for C# dev and Chinese translators.

#### Medium Priority

* Deploy multiple contracts to NEO TestNet

#### Low Priority

* Regression test again NEO TestNet via `neon-js`.

---

## References

TBA
