import random

def noun_nom_sg(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_noun_n_s=s.split()
    return random.choice(spisok_noun_n_s)

def noun_nom_pl(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_noun_n_p=s.split()
    return random.choice(spisok_noun_n_p)

def noun_acc(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_noun_a=s.split()
    return random.choice(spisok_noun_a)

def adj_nom_pl(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_adj_n_p=s.split()
    spisok_adj_n_p.append('')
    return random.choice(spisok_adj_n_p)

def verb_pl(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_verb_pl=s.split()
    return random.choice(spisok_verb_pl)

def verb_sg(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_verb_sg=s.split()
    return random.choice(spisok_verb_sg)

def souz(filename):
    with open (filename, encoding='utf-8') as f:
        s=f.read()
    spisok_souz=s.split()
    return random.choice(spisok_souz)

def otric():
    otric=['', 'не']
    return random.choice(otric)

def punct():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def sent1():
    sent=noun_nom_sg('noun_nomin_sg.txt')+ ' ' + otric()+' ' + verb_sg('verb_sg.txt') + ' ' + noun_acc('noun_acc_sg_pl.txt')
    return sent

def sent2():
    sent=adj_nom_pl('adj_nom_pl.txt')+ ' '+noun_nom_pl('noun_nomin_pl.txt') + ' ' + otric()+' ' + verb_pl('verb_pl.txt') + ' ' + noun_acc('noun_acc_sg_pl.txt')
    return sent

def make_sent():
    chislo = random.choice([1,2])
    if chislo == 1:
        sense=sent1()+','+' '+souz('souz.txt')+' '+sent2()+punct()+' '
        return sense.capitalize()
    else:
        sense=sent2()+','+' '+souz('souz.txt')+' '+sent1()+punct()+' '
        return sense.capitalize()

for n in range(5):
    print(make_sent(), end=' ')
