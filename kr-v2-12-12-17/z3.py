with open ('Ozhegov.txt', encoding='utf-8') as f:
    s = f.read()
    s=s.split("\n")
    spisok=[]
    while True:
        word = input().lower()
        if word == "":
            break
        else:
            spisok.append(word)
        for word1 in spisok:
            found = False
            for i in s:
                opred=i.split("|")
                if opred[0]==word:
                    found=True
                    break
        if found:
            print(opred[0]+" - "+opred[3]+" - "+opred[1])
        else:
            print("такое слово не нашлось")
