import random

def dict():
    with open('words.csv', encoding='utf-8') as f:
        d={}
        for line in f:
            line = line.replace('\n','').replace('\ufeff','')
            word, clue = line.split(';')
            if word in d:
                d[word].append(clue)
            else:
                d[word] = [clue]
    return d

def best_game():
    print ('Я умная программа и загадала существительное. Попробуй отгадать')
    print ('А еще я буду считать твои попытки')
    sel_word = random.choice(list(dict().keys()))
    sel_clue = random.choice(dict()[sel_word])
    print ('Подсказка: ',sel_clue, ' ...')
    atts = 0
    print ('Количество попыток: ', atts) 
    user_word = input().lower()
    while user_word != sel_word:
        if user_word == '':
            print ('Пока')
            break
        else:
            atts+=1
            print ('Не подходит. Попыток ты сделал уже: ', atts)
            user_word = input().lower()
    print ('Поздравляю! Ты угадал, красавчик.')
    onemoretime()
    
def onemoretime():
    print ('Если хочешь поиграть еще, только скажи "да", я с удовольствием')
    ans = input ().lower()
    if ans == 'да':
        best_game()
    else:
        print('Пока')

best_game()


