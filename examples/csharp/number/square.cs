using Neo.SmartContract.Framework;

// Date Created:                2018-03-07
// Date Modified:               2018-03-07
// Version:                     1
// Debug Contract Hash:         0xa90319238e843ab85f97c801026dd843e3e7fede
// Release Contract Hash:       0x605b2de2b665d919f2b26425ea2a90838e0b6322
// Available on NEO TestNet:    False
// Available on CoZ TestNet:    False
// Available on MainNet:        False

// Example  
// Input Params     :           02
// Output Params    :           02
// Operation Count  :           Contract compiled in Debug: 52 / Contract compiled in Release: 26
// GAS Consumption  :           Contract compiled in Debug:     0.038 (NEO Debugger) / 0.049 (neo-gui-developer)  
// GAS Consumption  :           Contract compiled in Release:   0.019 (NEO Debugger) / 0.030 (neo-gui-developer)

namespace SquareSmartContract
{
    public class Contract : SmartContract
    {
        public static int Main(int num)
        {
            var result = num * num;
            return result;
        }
    }
}