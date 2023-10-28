#!/usr/bin/env python3

import sys

input_query  = sys.argv[1]   #name of input datset "rand5-800"

submats = ['PAM30', 'PAM70', 'BLOSUM80', 'BLOSUM62']   #the possible submats associated with the file

for submat in submats:       

	file_of_interest = f'blast_{input_query}_v_qfo_{submat}.txt'#building a filename based on the known variables
	print(f'compiled filename: {file_of_interest}')
	with open(file_of_interest) as fh: 
		for line in fh:
			line = line.rstrip("\n") 
			if line.startswith('#'):
				continue 
			print(line)

	
