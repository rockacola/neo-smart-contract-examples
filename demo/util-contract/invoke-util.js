#!/usr/bin/env node

// -- Bootstrap

const Neon = require('@cityofzion/neon-js')
const Query = Neon.rpc.Query
const ContractParam = Neon.sc.ContractParam
const fixed82num = Neon.u.fixed82num
const hexstring2str = Neon.u.hexstring2str
const reverseHex = Neon.u.reverseHex
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
  UtilContract_2: 'c9ccb3ee3019357f4769d067d7e4783d41504673',
  UtilContract_3: 'e5551964312eff43cf15af057ff3aae4d4b8bfc9',
  UtilContract_7: '8322cac3d30094c947615c944e9d3734b6e467bc',
  UtilContract_9: '2ed7cb2fb83f5ed9c30177129da82475fbb2ac8a',
}
const rpcUrl = rpcUrls.testnetNeo2
const contract = contracts.UtilContract_9

// -- Chain of command

async function main () {
  console.log('== NeonJs Contract Invoke Demo - UtilContract ==')

  await rpcProfiles()
  await contractState()
  await versionDemo()
  // isOwnerDemo
  await magicNumberDemo()
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
  // myAddressDemo
  // targetAddressDemo
  // isAddressDemo
  // isWitnessAddressDemo

  console.log('== END ==')
  console.log()
}

// -- Methods

async function rpcProfiles() {
  try {
    console.log('getVersion:', (await Query.getVersion().execute(rpcUrl)).result.useragent)
  } catch (ex) {
    console.log('getVersion failed. err:', ex)
  }
  console.log('getBlockCount:', (await Query.getBlockCount().execute(rpcUrl)).result)
  console.log('getBestBlockHash:', (await Query.getBestBlockHash().execute(rpcUrl)).result)
}

async function contractState() {
  // -- GetContractState
  console.log()
  const contractStateResponse = await Query.getContractState(contract).execute(rpcUrl)
  // console.log('contractState:', contractState)
  console.log(`contractState name: [${contractStateResponse.result.name}], version: [${contractStateResponse.result.code_version}]`)
}

async function versionDemo() {
  console.log()
  console.log('UtilContract.version:')
  const response = await Query.invoke(contract, ContractParam.string('version')).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
  /**
   * Not showing expected result...
   */
}

async function magicNumberDemo() {
  console.log()
  console.log('UtilContract.magic_number:')
  const response = await Query.invoke(contract, ContractParam.string('magic_number')).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function magicStringDemo() {
  console.log()
  console.log('UtilContract.magic_string:')
  const response = await Query.invoke(contract, ContractParam.string('magic_string')).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function neoIdDemo() {
  console.log()
  console.log('UtilContract.neo_id:')
  const response = await Query.invoke(contract, ContractParam.string('neo_id')).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function addDemo() {
  console.log()
  console.log('UtilContract.add:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('add'), 
      ContractParam.array(ContractParam.integer(2), ContractParam.integer(3))
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function multiplyDemo() {
  console.log()
  console.log('UtilContract.multiply:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('multiply'), 
      ContractParam.array(ContractParam.integer(7), ContractParam.integer(6))
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function squareDemo() {
  console.log()
  console.log('UtilContract.square:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('square'),
      ContractParam.array(ContractParam.integer(11))
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function powerDemo() {
  console.log()
  console.log('UtilContract.power:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('power'),
      ContractParam.array(ContractParam.integer(2), ContractParam.integer(8))
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function fibonacciDemo() {
  console.log()
  console.log('UtilContract.fibonacci:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('fibonacci'),
      ContractParam.array(ContractParam.integer(10))
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function charCountDemo() {
  console.log()
  console.log('UtilContract.char_count:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('char_count'),
      ContractParam.array(ContractParam.string('internationalization'))
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function stringReverseDemo() {
  console.log()
  console.log('UtilContract.string_reverse:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('string_reverse'),
      ContractParam.array(ContractParam.string('live'))
    ).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
  /**
   * Expected rawValue:
   * '6e6f6974617a696c616e6f6974616e7265746e69'
   * Expected stringify value:
   * 'noitazilanoitanretni'
   */
}

async function arrayLengthDemo() {
  console.log()
  console.log('UtilContract.length:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('length'),
      ContractParam.array(
        ContractParam.string('a'),
        ContractParam.integer(2),
        ContractParam.boolean(true)
      )
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function addArrayDemo() {
  console.log()
  console.log('UtilContract.add_array:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('add_array'),
      ContractParam.array(
        ContractParam.integer(2),
        ContractParam.integer(3),
        ContractParam.integer(4)
      )
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], type: [${typeof(rawValue)}]`)
}

async function setStorageDemo() {
  console.log()
  console.log('UtilContract.set_storage:')

  const key = 'neon_test_key'
  const val = 'neon_test_' + Date.now()
  console.log('val:', val)

  const script = {
    scriptHash: contract,
    operation: 'set_storage',
    args: ContractParam.array(ContractParam.string(key), ContractParam.string(val))
  }
  const config = {
    net: 'TestNet',
    address: wallets.otto.address,
    privateKey: wallets.otto.wif,
    intents: Neon.api.makeIntent({ GAS: 0.001 }, wallets.otto.address), // NOTE: Seems that I must have an intent, so I send GAS to myself
    script,
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
  const response = await Query.invoke(
      contract,
      ContractParam.string('get_storage'),
      ContractParam.array(
        ContractParam.string('lorem'),
      )
    ).execute(rpcUrl)
  // console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
  /**
   * Expect: lorem_value
   */
}

async function blockHeightDemo() {
  console.log()
  console.log('UtilContract.height:')
  const response = await Query.invoke(contract, ContractParam.string('height')).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
  /**
   * Actual rawValue: 686569676874
   * Stringify to: height
   */
}

async function currentTimestampDemo() {
  console.log()
  console.log('UtilContract.current_timestamp:')
  const response = await Query.invoke(contract, ContractParam.string('current_timestamp')).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value[0].value
  console.log(`rawValue: [${rawValue}], stringify: [${hexstring2str(rawValue)}]`)
}

async function getTimestampDemo() {
  console.log()
  console.log('UtilContract.get_timestamp:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('get_timestamp'),
      ContractParam.array(ContractParam.integer(1))
    ).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value
  const ts = parseInt(rawValue) * 1000
  const dt = new Date(ts)
  console.log(`rawValue: [${rawValue}], dt: [${dt}]`)
}

async function getMerkleDemo() {
  console.log()
  console.log('UtilContract.get_merkle:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('get_merkle'),
      ContractParam.array(ContractParam.integer(1))
    ).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], reverseHex: [${reverseHex(rawValue)}]`)
  /**
   * Merkle of block 1: 8e3a32ba3a7e8bdb0ad9a2ad064713e45bd20eb0dab0d2e77df5b5ce985276d0
   */
}

async function getBlockHashDemo() {
  console.log()
  console.log('UtilContract.get_block_hash:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('get_block_hash'),
      ContractParam.array(ContractParam.integer(1))
    ).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], reverseHex: [${reverseHex(rawValue)}]`)
  /**
   * Hash of block 1: 0012f8566567a9d7ddf25acb5cf98286c9703297de675d01ba73fbfe6bcb841c
   */
}

async function getConsensusDemo() {
  console.log()
  console.log('UtilContract.get_consensus:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('get_consensus'),
      ContractParam.array(ContractParam.integer(1))
    ).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}]`)
  /**
   * ConsensusData of block 1: 12663300345212575697
   */
}

async function getNextConsensusDemo() {
  console.log()
  console.log('UtilContract.get_next_consensus:')
  const response = await Query.invoke(
      contract,
      ContractParam.string('get_next_consensus'),
      ContractParam.array(ContractParam.integer(1))
    ).execute(rpcUrl)
  // console.log('response:', response)
  // console.log('response.result.stack:', response.result.stack)
  // console.log('response.result.stack[0].value:', response.result.stack[0].value)
  const rawValue = response.result.stack[0].value
  console.log(`rawValue: [${rawValue}], reverseHex: [${reverseHex(rawValue)}]`)
  /**
   * Next Consensus of block 1: 257b026aecfe8e9878a2219a08b0f382b92d81f3
   */
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
