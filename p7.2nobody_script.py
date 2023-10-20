#!/usr/bin/env python3
import re

file_open = open('Python_07_nobody.txt','r') 
poem = file_open.read()
print(poem)
cat_poem = re.sub(r'Nobody','Schooner',poem)
print(cat_poem)

cat_file = open("Schooner.txt","w")
cat_file.write(cat_poem)


