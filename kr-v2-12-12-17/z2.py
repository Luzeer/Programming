#Задание2        
count=0
with open ('Ozhegov.txt', encoding='utf-8') as f:
    for line in f:
        splt_line=line.split("|")
        if len(splt_line[2])>0:
            count+=1
    print (count)
