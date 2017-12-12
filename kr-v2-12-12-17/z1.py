with open ('Ozhegov.txt', encoding='utf-8') as f:   
   for line in f:
        splt_line=line.split("|")
        if len(splt_line[0])>=20:
            print(line)
