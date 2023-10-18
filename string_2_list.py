#!/usr/bin/env python
taxa = 'sapiens, erectus, neanderthalensis'
taxa.split(',')
species = taxa.split(',')
print(species)
print(species[1])
print(type(species))
sorted(species)
print(sorted(species))
print(sorted(species, key=len))

