with open('text.txt', 'w', encoding='utf-8') as f:
    a=input('Введите слово')
    while a !='':
        a=input('Введите слово')
        if a[-3:]=='tur':
            f.write(a)
            f.write('\n')
