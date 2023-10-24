#!/usr/bin/env python3
import re


ecoli_contig = open('ecoli_0.25.contigs.fasta','r')
ecoli_contig_list = ecoli_contig.read()

print(ecoli_contig_list)

for headers in re.finditer(r">", ecoli_contig_list):

	print(headers)
	

	
