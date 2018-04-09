import re
 
def rfile(name):
    with open(name, 'r', encoding='utf-8') as f:
        return f.read()
 
def wfile(text,name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(str(text))
    if not f.writable:
        print('Файл недоступен')
 
def dinokot(text):
    f = r'\bдинозавр(\w{0,3})\b'
    r = r'кот\1'
    F = r'\bДинозавр(\w{0,3})\b'
    R = r'Кот\1'
    text = re.sub(f, r, text)
    text = re.sub(F, R, text)
    return text
                
name = input('Введите имя файла со статьей: ')
gotov = dinokot(rfile(name))
name = input('Введите имя файла для записи: ')
wfile (gotov, name)
