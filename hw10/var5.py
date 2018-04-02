import re
 
def readfile(name):
    with open(name, 'r', encoding='utf-8') as f:
        return f.read()
 
def writefile(text,name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text)
    if not f.writable:
        print('Файл недоступен')
 
def poisk(text):
    i = 0
    text = text.split('\n')
    for line in text:
        if re.search('Семейство', line):
            t = text[i]
            t = re.findall('[А-Я][а-я]+', t)
            i = 1
            for elem in t:
                if elem == 'Семейство':
                    return t[i]
            i+=1
name = input('Введите имя файла со статьей ')
stat = readfile(name)
sem = poisk(stat)
name = input('Введите имя файла для записи ')
writefile (sem,name)
