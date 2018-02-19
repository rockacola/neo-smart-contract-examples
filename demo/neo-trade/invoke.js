#!/usr/bin/env node

// -- Bootstrap

const Neon = require('@cityofzion/neon-js')
// const ScriptBuilder = Neon.sc.ScriptBuilder
const Query = Neon.rpc.Query
// const ContractParam = Neon.sc.ContractParam
// const fixed82num = Neon.u.fixed82num
// const hexstring2str = Neon.u.hexstring2str
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
  NeoTrade: 'b4abcc3a60cd94c16f38a145c27b9cd300791cc2',
}
const rpcUrl = rpcUrls.testnetNeo2
const contract = contracts.NeoTrade

// -- Chain of command

async function main () {
  console.log('== NeonJs Contract Invoke Demo - UtilContract ==')

  // console.log('Neon:', Neon)
  // console.log('ScriptBuilder:', ScriptBuilder);
  await doStuff()

  console.log('== END ==')
  console.log()
}

// -- Methods

async function doStuff() {
  const props = {
    scriptHash: contract,
    operation: 'balanceOfCurrency',
    args: [Neon.u.reverseHex('cef0c0fdcfe7838eff6ff104f9cdec2922297537')]
  }
  const script = Neon.sc.createScript(props)
  console.log('script:', script)
  
  const response = await Query.invokeScript(script).execute(rpcUrl)
  console.log('response:', response)
  console.log('response.result.stack:', response.result.stack)
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
