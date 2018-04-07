import re

def rfile():
    with open('mystem.xml', 'r', encoding='utf-8') as f:
        return f.read().split('\n')

def wfile(text):
    with open('out.txt', 'w', encoding='utf-8') as f:
        f.write(str(text))
    if not f.writable:
        print('Файл недоступен')

def diction(text):
    dict = {}
    for line in text:
        if re.search("[а-я]+", line, flags=re.IGNORECASE):
            j = 0
            l = re.search("gr=.+",line)
            for line1 in text:
                if line == line1:
                    j += 1
            dict[l] = j
    dict = sorted(dict.items(), key=lambda value: value[1])
    return (dict)

wfile(diction(rfile()))
