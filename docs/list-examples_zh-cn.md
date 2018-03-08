## 智能合约示例 Smart Contract Examples

编写智能合约来解决具体问题的代码示例种类

| 种类 | 名字 | 描述 | Python | C#
| --- | --- | --- | --- | ---
| Constant | Forty Two | 返回42,仅此而已 | [Source](../examples/python/constant/forty_two.py) | N/A
| Constant | Local Variable | 返回一个局部常数的字符串值 | N/A | N/A
| Constant | Global Variable | 返回一个全局常数的整数值 | N/A | N/A
| Constant | Global Variable 2 | 返回一个全局常数的字节数组 | N/A | N/A
| Constant | Echo | 返回其输入的值 | N/A | N/A
| Number | Add | 把两个输入的数字相加 | [Source](../examples/python/number/add.py) | N/A
| Number | Multiply | 把两个输入的数字相乘 | [Source](../examples/python/number/multiply.py) | N/A
| Number | Square | 返回一个输入数字的平方 | [Source](../examples/python/number/square.py) | N/A
| Number | Power | 基于输入数字的指数次幂 | [Source](../examples/python/number/power.py) | N/A
| Number | Fibonacci | 返回一个输入数字的斐波纳契值 | [Source](../examples/python/number/fibonacci.py) | N/A
| Number | Is Prime | 检查一个输入的数字是否一个素数 | N/A | N/A
| Number | Minimum | 找到两个输入数字中最小的那个 | N/A | N/A
| Number | Maximum | 找到两个输入数字中最大的那个 | N/A | N/A
| Number | Absolute | 取一个输入数字的绝对值 | N/A | N/A
| String | Character Count | 计算输入字符串的字符数 | [Source](../examples/python/string/character_count.py) | N/A
| String | String Reverse | 提供输入字符串的反向顺序 | [Source](../examples/python/string/string_reverse.py) | N/A
| String | String Explode | 将字符串拆分为具有指定分隔符字符串的数组 | N/A | N/A
| String | Take | ... | N/A | N/A
| Array | Array Length | 获取输入数组的长度 | [Source](../examples/python/array/array_length.py) | N/A
| Array | Array Sum | 从输入数字数组中汇总所有数字 | [Source](../examples/python/array/array_sum.py) | N/A
| Array | Array Reverse | 提供输入数组的反向顺序 | N/A | N/A
| Array | Array Implode | 使用指定的分隔符串将数组项连接成字符串 | N/A | N/A
| Array | Push | 在指定的数组中添加一个输入数字并将此数组返回 | N/A | N/A
| Array | Pop | 从指定数组中删除输入索引的值并返回 | N/A | N/A
| Array | Get Value | 从指定数组中获取输入索引的值 | N/A | N/A
| Array | Minimum | 找到输入int数组的最小的一个 | N/A | N/A
| Array | Maximum | 找到输入int数组的最大的一个 | N/A | N/A
| Array | Range | ... | N/A | N/A
| Iterator | While Breaker | ... | N/A | N/A
| Bytes | ... | ... | N/A | N/A
| Encode | Integer to String | 将输入数转换成字符串格式 | [Source](../examples/python/encode/int2str.py) | N/A
| Encode | SHA1 | ... | N/A | N/A
| Encode | SHA256 | ... | N/A | N/A
| Encode | HASH160 | ... | N/A | N/A
| Encode | HASH256 | ... | N/A | N/A
| Storage | Storage Echo | ... | N/A | N/A
| Block | Current Height | 获得当前区块高度 | [Source](../examples/python/block/current_height.py) | N/A
| Block | Current Timestamp | 获得当前区块的时间戳 | [Source](../examples/python/block/current_timestamp.py) | N/A
| Block | Block Timestamp | 获得一个给定区块高度的时间戳 | [Source](../examples/python/block/block_timestamp.py) | N/A
| Block | Block Index | ... | N/A | N/A
| Block | Block Version | ... | N/A | N/A
| Block | Block Merkle Root | 获得一个给定的区块高度的默克尔根 | [Source](../examples/python/block/block_merkle_root.py) | N/A
| Block | Block Previous Hash | ... | N/A | N/A
| Block | Block Hash | 获得一个给定区块高度的哈希值 | [Source](../examples/python/block/block_hash.py) | N/A
| Block | Block Consensus | 获得一个给定区块高度的共识值 | [Source](../examples/python/block/block_consensus.py) | N/A
| Block | Next Consensus | 获得一个给定区块高度的下一个共识值 | [Source](../examples/python/block/next_consensus.py) | N/A
| Block | Block Transaction Count | ... | N/A | N/A
| Block | Block Transactions | ... | N/A | N/A
| Block | Block Transaction | ... | N/A | N/A
| Account | My Address | 获取合约调用者的地址 | N/A | N/A
| Account | Target Address | 获取合约目标的地址 | N/A | N/A
| Account | Is Owner | 检查调用者的地址是否与静态地址匹配 | [Source](../examples/python/account/is_owner.py) | N/A
| Account | Is Address | 检查调用者的地址是否与输入地址匹配 | N/A | N/A
| Account | Is Address (Witness) | 检查调用者的地址是否在鉴证人列表中(通过checkwitness方法) | N/A | N/A
| Account | Get Hash | ... | N/A | N/A
| Account | Get Votes | ... | N/A | N/A
| Contract | Get Contract | ... | N/A | N/A
| Contract | Get Contract Script | ... | N/A | N/A
| Contract | Get Contract Storage Context | ... | N/A | N/A
| Contract | Destroy Contract | ... | N/A | N/A
| Blockchain | Get Balance | ... | N/A | N/A
| Blockchain | Register App Call | ... | N/A | N/A
| Blockchain | Dynamic App Call | ... | N/A | N/A
| Validation | ... | ... | N/A | N/A
| Random | ... | ... | N/A | N/A
| Optimization | Condition Positions | 演示条件语句的位置如何影响GAS消耗 | N/A | N/A
| Optimization | Recursive vs Iterator | 演示使用循环与递归实现的相同逻辑的GAS消耗| N/A | N/A
| Optimization | Cost of Notify | ... | N/A | N/A
| Optimization | Throw if Null | ... | N/A | N/A
| Optimization | Exception Handling | ... | N/A | N/A
