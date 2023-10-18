#!/usr/bin/env python
import sys
dna = sys.argv[1]
dna = dna.upper()
dna.count('A')
print(dna.count('A'))
dna.count('T')
print(dna.count('T'))
ATcontent = (dna.count('A') + dna.count('T')) / len(dna) * 100 
print(ATcontent ,  'AT%')
dna.count('G')
print(dna.count('G'))
dna.count('C')
print(dna.count('C'))
GCcontent = (dna.count('G') + dna.count('C')) / len(dna) * 100
print(GCcontent ,  'GC%')
