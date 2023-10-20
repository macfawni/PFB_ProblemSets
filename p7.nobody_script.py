#!/usr/bin/env python3
import re

nobody = open('Python_07_nobody.txt', 'r')
poem = nobody.read()

print(poem)

for found in re.finditer(r"Nobody", poem):
	print(found)

