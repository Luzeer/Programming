def opred(target):
    target = target.capitalize()
    with open ('Ozhegov.txt', encoding='utf-8') as f:
       for line in f:
            splt_line1=line.split("|")
            word1=splt_line1[0]
            if word1 == target:
                opred=splitted_line[1]
            else:
                opred='Не найдено'
                return(opred)

while 1:
    target=input()
    if target =='':
        break
    print(opred(target))
