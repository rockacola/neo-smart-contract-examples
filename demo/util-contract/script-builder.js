#!/usr/bin/env node

// -- Bootstrap

const Neon = require('@cityofzion/neon-js')
const Query = Neon.rpc.Query
const createScript = Neon.sc.createScript
// const ContractParam = Neon.sc.ContractParam
const fixed82num = Neon.u.fixed82num
const hexstring2str = Neon.u.hexstring2str
// const reverseHex = Neon.u.reverseHex
const rpcUrls = {
  testnetNeo2: 'http://seed2.neo.org:20332',
  testnetNeo4: 'http://seed4.neo.org:20332',
  mainnetNeo2: 'http://seed2.neo.org:10332',
  mainnetNeo3: 'http://seed3.neo.org:10332', // Mainnet running old Neo version
  privnet: 'http://127.0.0.1:30333',
}
const wallets = {
  otto: {
    address: 'AHY2eXXtkdxJ4nAJ9sWSP5n83B7nPWqBnb',
    wif: 'KwW2MiwwVJoDCaFZw3M6iv9vtXFJtMH6Un69Sw4ZBoMYsMyBmuMG'
  }
}
const contracts = {
  UtilContract_9: '2ed7cb2fb83f5ed9c30177129da82475fbb2ac8a',
}
const rpcUrl = rpcUrls.testnetNeo2
const contract = contracts.UtilContract_9

// -- Chain of command

async function main () {
  console.log('== NeonJs ScriptBuilder Demo - UtilContract ==')

  await versionDemo()
  await isOwnerDemo() // No desirable data from response
  await magicNumberDemo() // Buggy response
  await magicStringDemo()
  await neoIdDemo()
  await addDemo()
  await multiplyDemo()
  await squareDemo()
  await powerDemo()
  await fibonacciDemo()
  await charCountDemo()
  await stringReverseDemo()
  await arrayLengthDemo()
  await addArrayDemo()
  await setStorageDemo()
  await getStorageDemo()
  await blockHeightDemo()
  await currentTimestampDemo()
  await getTimestampDemo()
  await getMerkleDemo()
  await getBlockHashDemo()
  await getConsensusDemo()
  await getNextConsensusDemo()
  await myAddressDemo() // No desirable data from response
  // targetAddressDemo
  // isAddressDemo
  // isWitnessAddressDemo

  console.log('== END ==')
  console.log()
}

// -- Methods

async function versionDemo() {
  console.log()
  console.log('UtilContract.version:')

  const props = {
    scriptHash: contract,
    operation: 'version',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function isOwnerDemo() {
  console.log()
  console.log('UtilContract.is_owner:')

  const props = {
    scriptHash: contract,
    operation: 'is_owner',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  console.log('response:', response)
  /**
   * Actual response:
    { jsonrpc: '2.0',
      id: 1234,
      result:
      { script: '00c10869735f6f776e6572678aacb2fb7524a89d127701c3d95e3fb82fcbd72e',
        state: 'FAULT, BREAK',
        gas_consumed: '0.335',
        stack: [] } }
   */
}

async function magicNumberDemo() {
  console.log()
  console.log('UtilContract.magic_number:')

  const props = {
    scriptHash: contract,
    operation: 'magic_number',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], fixed82num: [${fixed82num(rawValue)}]`)
}

async function magicStringDemo() {
  console.log()
  console.log('UtilContract.magic_string:')

  const props = {
    scriptHash: contract,
    operation: 'magic_string',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function neoIdDemo() {
  console.log()
  console.log('UtilContract.neo_id:')

  const props = {
    scriptHash: contract,
    operation: 'neo_id',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
  /**
   * Actual: 9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc5
   * TODO: turn hash value into wallet address
   */
}

async function addDemo() {
  console.log()
  console.log('UtilContract.add:')

  const props = {
    scriptHash: contract,
    operation: 'add',
    args: [2, 3]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function multiplyDemo() {
  console.log()
  console.log('UtilContract.multiply:')

  const props = {
    scriptHash: contract,
    operation: 'multiply',
    args: [7, 6]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function squareDemo() {
  console.log()
  console.log('UtilContract.square:')

  const props = {
    scriptHash: contract,
    operation: 'square',
    args: [11]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function powerDemo() {
  console.log()
  console.log('UtilContract.power:')

  const props = {
    scriptHash: contract,
    operation: 'power',
    args: [2, 8]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function fibonacciDemo() {
  console.log()
  console.log('UtilContract.fibonacci:')

  const props = {
    scriptHash: contract,
    operation: 'fibonacci',
    args: [10]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function charCountDemo() {
  console.log()
  console.log('UtilContract.char_count:')

  const props = {
    scriptHash: contract,
    operation: 'char_count',
    args: [{ "type": "String", "value": "internationalization" }]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function stringReverseDemo() {
  console.log()
  console.log('UtilContract.string_reverse:')

  const props = {
    scriptHash: contract,
    operation: 'string_reverse',
    args: [{ "type": "String", "value": "live" }]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function arrayLengthDemo() {
  console.log()
  console.log('UtilContract.length:')
  
  const props = {
    scriptHash: contract,
    operation: 'length',
    args: [
      { "type": "String", "value": "a" },
      { "type": "Integer", "value": 2 },
      { "type": "Boolean", "value": true }, // NOTE: This throws error when value is false, likely a neon-js bug
    ]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function addArrayDemo() {
  console.log()
  console.log('UtilContract.add_array:')

  const props = {
    scriptHash: contract,
    operation: 'add_array',
    args: [2, 3, 4]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function setStorageDemo() {
  console.log()
  console.log('UtilContract.set_storage:')

  const key = 'neon_sb_key'
  const val = 'neon_sb_' + Date.now()
  console.log('val:', val)

  const props = {
    scriptHash: contract,
    operation: 'set_storage',
    args: [
      { "type": "String", "value": key },
      { "type": "String", "value": val },
    ]
  }
  const config = {
    net: 'TestNet',
    address: wallets.otto.address,
    privateKey: wallets.otto.wif,
    intents: Neon.api.makeIntent({ GAS: 0.001 }, wallets.otto.address), // NOTE: Seems that I must have an intent, so I send GAS to myself
    script: props,
    gas: 0
  }

  const response = await Neon.api.doInvoke(config)
  // console.log('response:', response)
  if (response.response.result === false) {
    console.log('doInvoke() failed')
    return;
  }

  console.log(`doInvoke() success. TX: [${response.response.txid}], `)
  // console.log('response.tx:', response.tx)
}

async function getStorageDemo() {
  console.log()
  console.log('UtilContract.get_storage:')

  const key = 'neon_sb_key'
  const props = {
    scriptHash: contract,
    operation: 'get_storage',
    args: [
      { "type": "String", "value": key },
    ]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function blockHeightDemo() {
  console.log()
  console.log('UtilContract.height:')

  const props = {
    scriptHash: contract,
    operation: 'height',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function currentTimestampDemo() {
  console.log()
  console.log('UtilContract.current_timestamp:')

  const props = {
    scriptHash: contract,
    operation: 'current_timestamp',
    args: []
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function getTimestampDemo() {
  console.log()
  console.log('UtilContract.get_timestamp:')

  const blockHeight = 1
  const props = {
    scriptHash: contract,
    operation: 'get_timestamp',
    args: [blockHeight]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function getMerkleDemo() {
  console.log()
  console.log('UtilContract.get_merkle:')

  const blockHeight = 1
  const props = {
    scriptHash: contract,
    operation: 'get_merkle',
    args: [blockHeight]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function getBlockHashDemo() {
  console.log()
  console.log('UtilContract.get_block_hash:')

  const blockHeight = 1
  const props = {
    scriptHash: contract,
    operation: 'get_block_hash',
    args: [blockHeight]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function getConsensusDemo() {
  console.log()
  console.log('UtilContract.get_consensus:')

  const blockHeight = 1
  const props = {
    scriptHash: contract,
    operation: 'get_consensus',
    args: [blockHeight]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function getNextConsensusDemo() {
  console.log()
  console.log('UtilContract.get_next_consensus:')

  const blockHeight = 1
  const props = {
    scriptHash: contract,
    operation: 'get_next_consensus',
    args: [blockHeight]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function myAddressDemo() {
  console.log()
  console.log('UtilContract.my_address:')

  const props = {
    scriptHash: contract,
    operation: 'my_address',
    args: []
  }
  const config = {
    net: 'TestNet',
    address: wallets.otto.address,
    privateKey: wallets.otto.wif,
    intents: Neon.api.makeIntent({ GAS: 0.001 }, wallets.otto.address), // NOTE: Seems that I must have an intent, so I send GAS to myself
    script: props,
    gas: 0
  }

  const response = await Neon.api.doInvoke(config)
  // console.log('response:', response)
  if (response.response.result === false) {
    console.log('doInvoke() failed')
    return;
  }

  console.log(`doInvoke() success. TX: [${response.response.txid}], `)
  // console.log('response.tx:', response.tx)

}

// -- Execute

/**
 * Toggle to provide promise reject trace.
 */
const ENABLE_LOG_UNHANDLED_REJECTION = true
if (ENABLE_LOG_UNHANDLED_REJECTION) {
  process.on('unhandledRejection', (reason, p) => {
    console.log('Unhandled Rejection at: Promise', p, 'reason:', reason)
  })
}

main()
