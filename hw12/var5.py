import os

def splitting(dir_name, splitter, long_named_dirs):
    cnt_long_named_dirs = 0
    dir_name_splitted = dir_name.split(splitter)
    words_in_dir_name = 0
    new_dir_name = []
    for elem in dir_name_splitted:
        if (elem != ' '):
            words_in_dir_name += 1
            
    if (words_in_dir_name >= 2):
        cnt_long_named_dirs += 1
        long_named_dirs.append(dir_name)
    elif (splitter != "_"):
        cnt_long_named_dirs += splitting(dir_name, "_", long_named_dirs)
    elif (splitter != "." and splitter != "_"):
        cnt_long_named_dirs += splitting(dir_name, ".", long_named_dirs)
    return cnt_long_named_dirs

file_list = os.listdir()
file_list = sorted(file_list)

long_named_dirs = []
cnt_long_named_dirs = 0

for file in file_list:
    if (os.path.isdir(file)):
        dir_name = file
        cnt_long_named_dirs += splitting(dir_name, " ", long_named_dirs)
        
print(cnt_long_named_dirs)
print()
for elem in long_named_dirs:
    print(elem)
