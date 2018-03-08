


#### Constant

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/local_variable.py test ff 07 False False
```

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
