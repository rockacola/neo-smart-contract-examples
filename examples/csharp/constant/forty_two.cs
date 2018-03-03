using Neo.SmartContract.Framework;

// Date Created:               2018-03-03
// Date Modified:              2018-03-03
// Version:                    1
// Contract Hash:              ee8bf881332c5cd7c5d91d3cdeae9ede33c8df7f
// Available on NEO TestNet:   False
// Available on CoZ TestNet:   False
// Available on MainNet:       False

// Example:
// Test Invoke:                 ???
// Expected Result:             42
// Operation Count:             23
// GAS Consumption:             0.016

namespace Return42SmartContract
{
    public class Contract : SmartContract
    {
        public static int Main()
        {
            return 42; // Direct return an integer without usage of local variable
        }
    }
}
