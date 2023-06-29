

def generate_note(ip):
    with open("data/usage.md","r") as f:
        content = f.read()
    content = content.format(ip=ip)
    with open("usage.md","w") as f:
        f.write(content)
