#!/usr/bin/env python
import sys
dna = sys.argv[1]
dna = dna.upper()
dna.count('T')
print("num T:" , dna.count('T'))
dna.count('G')
print("num G:" , dna.count('G'))
dna.count('A')
print("num A:" , dna.count('A'))
dna.count('C')
print("num C:" , dna.count('C'))
