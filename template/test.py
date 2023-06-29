#!/usr/bin/python3

with open('file.txt',"r") as f:
    content = f.read()

content = content.replace('{','{{')
content = content.replace('}','}}')

print(content)

