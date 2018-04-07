import re

def rfile():
    with open('mystem.xml', 'r', encoding='utf-8') as f:
        return f.read().split('\n')

def wfile(text):
    with open('out.txt', 'w', encoding='utf-8') as f:
        f.write(str(text))
    if not f.writable:
        print('Файл недоступен')

def count(text):
    coun=0
    a=1
    for line in text:
        if re.search('</body>',line):
            a*=-1
        if a==-1:
            coun+=len(line)
        if re.search('<body>',line):
            flag*=-1
    return coun 
 
wfile(count(rfile()))
