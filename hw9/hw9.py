import re

filename = input('Откуда читать: ')
resultfilename = input('КУда записать: ')
with open(filename, "r", encoding="utf-8") as f:
    text = f.read().lower().replace('\n', ' ').replace('\t', ' ')
with open(resultfilename, "w", encoding="utf-8") as f:
    f.write(str(re.findall("cъе[а-я]", text)))
    f.write(str(re.findall("съе[а-я][а-я]", text)))
    f.write(str(re.findall("съе[а-я][а-я][а-я]", text)))
    f.write(str(re.findall("съе[а-я][а-я][а-я][а-я]", text)))
    f.write(str(re.findall("съе[а-я][а-я][а-я][а-я][а-я]", text)))
    f.write(str(re.findall("съе[а-я][а-я][а-я][а-я][а-я][а-я]", text)))
    f.write(str(re.findall("съе[а-я][а-я][а-я][а-я][а-я][а-я][а-я]", text)))
if not f.writable:
    print("Проблемка с файлом")
