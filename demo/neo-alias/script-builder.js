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
  },
  ayu: {
    address: 'AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',
  },
}
const contracts = {
  NeoAlias_17: '8a092d91a822192b20e91722dc3dea28dfdb5cbd',
}
const rpcUrl = rpcUrls.testnetNeo2
const contract = contracts.NeoAlias_17

// -- Chain of command

async function main () {
  console.log('== NeonJs ScriptBuilder Demo - NeoAlias ==')

  // await versionDemo()
  // await isOwnerDemo() // No desirable data from response
  // await countAllDemo()
  // await countAliasDemo()
  // await getAliasDemo()
  // await setAliasDemo()
  // await getAliasScoreDemo()
  await voteAliasDemo()

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

async function countAllDemo() {
  console.log()
  console.log('UtilContract.count_all:')

  const props = {
    scriptHash: contract,
    operation: 'count_all',
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

async function countAliasDemo() {
  console.log()
  console.log('UtilContract.count_alias:')

  const props = {
    scriptHash: contract,
    operation: 'count_alias',
    args: [{ "type": "String", "value": wallets.ayu.address }]
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function getAliasDemo() {
  console.log()
  console.log('UtilContract.get_alias:')

  const props = {
    scriptHash: contract,
    operation: 'get_alias',
    // args: [
    //   { "type": "String", "value": "AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy" },
    //   { "type": "Integer", "value": 1 }, // There 'may be' a problem dealing with zero
    // ],
    args: [
      { "type": "String", "value": wallets.ayu.address },
      { "type": "String", "value": '0' }, // Use string may workaround it
    ],
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function setAliasDemo() {
  console.log()
  console.log('UtilContract.set_alias:')

  const newAlias = 'ayu_' + Date.now()
  console.log('newAlias:', newAlias)
  const invokerAddr = wallets.otto.address
  // const invokerAddr = Neon.u.reverseHex(Neon.wallet.getScriptHashFromAddress(wallets.otto.address)) // 1351f0fbad8bfff9629f269081972e97c8e87441
  console.log('invokerAddr:', invokerAddr)
  const props = {
    scriptHash: contract,
    operation: 'set_alias',
    args: [
      { "type": "String", "value": invokerAddr },
      { "type": "String", "value": wallets.ayu.address },
      { "type": "String", "value": newAlias },
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

async function getAliasScoreDemo() {
  console.log()
  console.log('UtilContract.get_alias_score:')

  const props = {
    scriptHash: contract,
    operation: 'get_alias_score',
    args: [
      { "type": "String", "value": wallets.ayu.address },
      { "type": "String", "value": '0' }, // Use string may workaround it
    ],
  }
  const script = Neon.sc.createScript(props)
  // console.log('script:', script)
  const response = await Query.invokeScript(script).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
}

async function voteAliasDemo() {
  console.log()
  console.log('UtilContract.vote_alias:')

  const point = '1'
  const invokerAddr = wallets.otto.address
  // const invokerAddr = Neon.u.reverseHex(Neon.wallet.getScriptHashFromAddress(wallets.otto.address)) // 1351f0fbad8bfff9629f269081972e97c8e87441
  console.log('invokerAddr:', invokerAddr)
  const props = {
    scriptHash: contract,
    operation: 'vote_alias',
    args: [
      { "type": "String", "value": invokerAddr },
      { "type": "String", "value": wallets.ayu.address },
      { "type": "String", "value": point },
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
