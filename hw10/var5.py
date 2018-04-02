import re
 
def rfile(name):
    with open(name, 'r', encoding='utf-8') as f:
        return f.read()
 
def wfile(text,name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(str(text))
    if not f.writable:
        print('Файл недоступен')
 
def poisk(text):
    i = 0
    text = text.split('\n')
    for st in text:
        if re.search('Семейство', st):
            t = text[i]
            t = re.findall('[А-Я][а-я]+', t)
            i = 1
            for elem in t:
                if elem == 'Семейство':
                    return t[i]
            i+=1
            
name = input('Введите имя файла со статьей: ')
stat = rfile(name)
sem = poisk(stat)
name = input('Введите имя файла для записи: ')
wfile (sem, name)
