with open('text.txt', 'w', encoding='utf-8') as f:
    a=input()
    while a !='':
        a=input()
        if a[-3:]=='tur':
            f.write(a)
            f.write('\n')
