import re
import collections
import os

def readfile (name):
    for i in name:
        f_in = open(i, "r", encoding='utf-8')
        text = f_in.read()
        parsetext(text, i)
    
def parsetext(text, filename):
    f_out = open(filename[: filename.find(".html", 0, len(filename))]+".txt", "w", encoding='cp1251')
    text = text.split("\n")
    for line in text:
        index_newsname_start = line.find("<title>", 0, len(line))
        index_newsname_end = line.find("</title>", 0, len(line))
        if (index_newsname_start != -1):
            f_out.write(line[index_newsname_start + len("<title>") : index_newsname_end] + "\n")
        index_text_start = line.find("</ana>", 0, len(line))
        index_text_end = line.find("</w>", 0, len(line))
        index_sign_end = line.find("</se", index_text_end, len(line))
        word = ""
        if (index_text_start != -1):
            word = line[index_text_start + len("</ana>") : index_text_end]
            word = word.replace("`", "")
            if (index_sign_end != -1):
                sign = line[index_text_end + len("</w>") : index_sign_end]
                sign = sign.replace(" .", ".")
                word += sign
            f_out.write(word + " ")
        if (line.find("</se>", 0, len(line)) != -1):
            f_out.write("\n")

filelist = []
ls = os.listdir()
for file in ls:
    if (file.find(".html", 0, len(file)) != -1):
        filelist.append(file)
        
readfile(filelist)
