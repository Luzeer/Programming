import re
import os
import collections

def readfile (name):
    text=''
    for i in name:
        with open(i, 'r', encoding='utf-8') as f:
            text+=f.read()
    return text

def countproper (text):
    propnoun=re.findall("lex=\"[А-Я][а-я\-]+",text)
    propnoun=collections.Counter(propnoun)
    with open('ex2.txt', 'w', encoding='cp-1251') as f:
        for key,value in propnoun.items():
            f.write(key[5:])
            f.write('\t')
            f.write(str(value))
            f.write('\n')
            
filelist = []
ls = os.listdir()
for file in ls:
    if (file.find(".html", 0, len(file)) != -1):
        filelist.append(file)
countproper(readfile(filelist))
