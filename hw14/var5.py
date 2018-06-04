file = open('file.txt', 'r', encoding='UTF8')
text = file.read()
sentences = text.replace('?', '.').replace('!', '.').replace(',', '').split('.')
tex = [word.split(' ') for word in sentences]
#print(words_in_sent)

def count_char_in_word(haystack, needle):
    count = 0
    i = -1
    while True:
        i = haystack.find(needle, i+1)
        if i == -1:
            return count
        count += 1

    
new_list = [[[char * count_char_in_word(word, char) for char in word] 
             for word in sent]
            for sent in tex]

for word in new_list:
    for list in word:
        print(''.join(list), end=' ')
    print()
