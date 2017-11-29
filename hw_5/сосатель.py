n = input('введите свое имя: ')
with open('text.txt', 'w', encoding='utf-8') as f:
    a=input('введите свое послание Лиле: ')
    while a !='':
        a=input('введите свое послание Лиле: ')
        #print(a)
        if a[-3:]=='хуй':
            print('сама соси,', n)
            break
