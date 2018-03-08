using Neo.SmartContract.Framework;

// Date Created:               2018-03-03
// Date Modified:              2018-03-03
// Version:                    1
// Debug Contract Hash:        0xee8bf881332c5cd7c5d91d3cdeae9ede33c8df7f
// Release Contract Hash:      0xdd4db0e2e009652274178d1dd14c543418282334
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
