#!/usr/bin/env python3

#Python_file = open("Python_06.txt","r")
#contents = Python_file.read()
#print(contents, type(contents))
#for line in contents:
#	print(line, type(line))
#	line = line.upper()
#	print(line)

with open("Python_06.txt","r") as Buried_Treasure, open("Python_06.uc.txt","w") as Buried_Treasure_UC:

	for line in Buried_Treasure:
		line = line.upper()
		print(line)
		Buried_Treasure_UC.write(f'{line:}')
