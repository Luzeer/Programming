import re
import collections

def rfile():
    with open('mystem.xml', 'r', encoding='utf-8') as f:
        return f.read()

def wfile(text):
    with open('out.txt', 'w', encoding='utf-8') as f:
        f.write(str(text))
    if not f.writable:
        print('Файл недоступен')
        
def diction(text):        
    forms=re.findall(r'gr="(.*)"', text)
    dict={}
    for a in forms:
        if a in dict:
            val=dict[a]
            dict[a]=val+1
        else:
            dict[a]=1
    dict=sorted(dict)
    
    for key in dict:
        print(key)
    return (dict)

wfile(diction(rfile()))
