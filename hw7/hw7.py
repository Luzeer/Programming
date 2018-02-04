#var5
import collections

def file(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
    for i in ['.',',','?','!',';',':','"','- ','-','—','(',')',"'",'”','’']: 
        text = text.replace(i,'')
    text = text.lower()
    words = text.split()
    return words

def adj_ous(name):
    adj_ous = []
    for word in file(name):
        if word.endswith('ous'):
            adj_ous.append(word)
    return adj_ous

def length(name):
    length = {}
    for word in adj_ous(name):
    	length[word] = len(word)
    return length

def middle_len(name):
    s=0
    for value in length(name).values():
        s+=value
    if len(length(name))==0:
        ml=0
    else:
        ml=s/len(length(name))
    return ml

def adj_print(name):
    print ('В тексте ', len(length(name)), ' прилагательных с суффиксом -ous-.')
    print('Их средняя длина: ', middle_len(name))


adj_print(input('Введите название файла: '))
