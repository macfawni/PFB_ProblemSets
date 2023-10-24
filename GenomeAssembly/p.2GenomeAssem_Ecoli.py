#!/usr/bin/env python3

import re

ecoli_contig = open('ecoli_0.25.contigs.fasta','r')
ecoli_contig_list = ecoli_contig.read()
#print(ecoli_contig_list)

Ecoli = ecoli_contig_list.split('>')
#print(Ecoli)
#print(len(Ecoli))



for contigs in Ecoli:
	whatever = contigs.split('\n')
	print(whatever)  
	whatever2 = ''.join(Ecoli[1:])
	print(whatever2)
