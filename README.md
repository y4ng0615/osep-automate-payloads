## 准备

1. 在kali上安装smb, 开启smb服务，让windows可以访问文件
```
sudo apt install samba
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.old
sudo nano /etc/samba/smb.conf
```
```
[visualstudio]
 path = /home/kali/data
 browseable = yes
 read only = no
```
```
sudo smbpasswd -a kali
sudo systemctl start smbd

mkdir /home/kali/data
chmod -R 777 /home/kali/data
```

2. 在Windows上安装Visual Studio

3. 将输出文件out链接到/var/www/html(可能需要修改apache配置文件，允许访问软链接)，将工具放在/var/www/html/tools (可能需要修改权限)
```
ln -s ./out /var/www/html
mkdir /var/www/html/tools
```

4. 根据自己在/var/www/html中的工具，修改data/usage.md，脚本会自动修改ip

## 使用方法

![GIF 2023-7-8 16-47-19](https://github.com/seagate-1/osep-automate-payloads/assets/60332241/41e639d0-ed44-43d7-a587-17e6e1cb9822)

1. 运行 参数为指定网卡
```
./Generator.py tun0
./Generator.py eth0
```

2. 切换到Windows打开payloads/payloads.sln，重新生成

3. 切换回kali，继续运行

4. 打开usage.md，直接对命令进行复制粘贴

按提示在windows上打开payloads.sln,编译程序(可能需要修改生成程序的路径)

所有结果都生成在out中

所有url和命令都在usage.md,直接复制命令


## C\#
- [x] inject 进程注入 exe
- [x] hollowing exe
- [x] inject dll
- [x] hollowing dll
- [x] Dotnet2jscript inject dll
- [x] Dotnet2jscript hollowing dll
- [x] BypassCLM exe 
`C:\Windows\Microsoft.NET\Framework64\v4.0.30319\installutil.exe /logfile= /LogToConsole=false /U C:\Users\admin\Desktop\BypassCLM.exe`
- [x] aspx
- [X] compiler绕过白名单
- [ ] Installer直接反弹shell绕过白名单 **有点问题 wmi的正常**

---
## ps1
- [x] inject.ps1 直接注入
- [x] reflection.ps1 powershell反射 inject/hollow
- [x] netreflection.ps1net反射dll <span style="color:red">__路径可能需要修改__</span>
- [x] msfvenom直接生成的 

---
## vba
- [x] loader.vba 普通方法 x86
- [x] vba执行powershell 调用WMI 6.8.2 可以是x64 必须修改为runner.doc

---
## hta
- [x] 绕过白名单

---
## xsl
- [x] Compiler白名单绕过
http://<ip>/other/test.xml
http://<ip>/other/test.txt
- [X] wmic执行powershell 放到了Csharp中

---
## 使用的payload

windows/x64/meterpreter/reverse_https

windows/x64/meterpreter/reverse_https thread

windows/meterpreter/reverse_https

windows/meterpreter/reverse_https thread

---

seagate_yang@163.com




