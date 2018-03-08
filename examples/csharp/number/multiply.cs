using Neo.SmartContract.Framework;

// Date Created:                2018-03-06
// Date Modified:               2018-03-06
// Version:                     1
// Debug Contract Hash:         0x208d537c170d97927f30f1ad59039d0f50061de1 
// Release Contract Hash:       0x3df1e6c8226b1ea2c2c88e1a061a98d1071a1b87
// Available on NEO TestNet:    False
// Available on CoZ TestNet:    False
// Available on MainNet:        False

// Example  
// Input Params     :           0202
// Output Params    :           02
// Operation Count  :           Contract compiled in Debug: 60 / Contract compiled in Release: 34
// GAS Consumption  :           Contract compiled in Debug:     0.043 (NEO Debugger) / 0.054 (neo-gui-developer)  
// GAS Consumption  :           Contract compiled in Release:   0.024 (NEO Debugger) / 0.035 (neo-gui-developer)

namespace SumSmartContract
{
    public class Contract : SmartContract
    {
        public static int Main(int a, int b)
        {
            var c = a * b;
            return c;
        }
    }
}