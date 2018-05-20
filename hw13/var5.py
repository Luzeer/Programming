import os

def func(names, starting_path):
	for root, dirs, files in os.walk(starting_path):
		for file in files:
			name, extension = os.path.splitext(file)
			if name not in names:
				names.append(name)
		if dirs != []:	
			for d in dirs:
				func(names, start_path + d)
	return names

names_list = func([], '.')
print(names_list)
print(len(names_list))
