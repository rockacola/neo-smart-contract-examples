using Neo.SmartContract.Framework;

// Date Created:                2018-03-03
// Date Modified:               2018-03-03
// Version:                     1
// Debug Contract Hash:         0x4f088dab7a5167adeda956881c213ace55b64ebd 
// Release Contract Hash:       0x0860b720fa7a40312289ee94c6e0cadcc9251eed
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
            var c = a + b;
            return c;
        }
    }
}