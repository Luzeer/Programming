#var5
print('Как работает программа: 1.Введите текст в файл text.txt в кодировке utf-8, сохраните, 1.1. Файл и программа должны лежать в одной папке, 2.Запустите программу')


with open ('text.txt', encoding='utf-8') as f:
    s=f.read()
if s == "":
    print('Хватит запускать сюда пустые строки, вы же не дураки, ну')
s=s.replace(',','').replace('.','').replace('?', '').replace('-', '').replace('(', '').replace(')', '').replace('!', '').replace(':', '')
s=s.lower() #для красоты, чтобы все было с маленькой буквы
s=s.split()
#print(s) #Включить, если нужно посмотреть получившийся список первоначального текста без знаков препинания
count=0
for i in range (len(s)):
    if len(s[i])>10:
        count+=1
        #print(s[i]) #Включить, если нужно посмотреть подошедшие слова
if count == 0:
    print ('Хватит запускать сюда пустые строки и файлы. Если же в файле есть текст, то там нет слов с длиной больше 10 символов')
else:
    print (round(count/len(s)*100, 2),'% cлов имеет длину больше 10 символов. Возможны погрешности, если попались знаки препинания, которые я не учла.')
