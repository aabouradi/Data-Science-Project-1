#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:12:33 2022

@author: abdullahabouradi
"""

import dna_rna

DNAseq = 'GTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCT'

RNAseq = (dna_rna.DNAtoRNA(DNAseq))

print(RNAseq)
print(dna_rna.RNAtoDNA(RNAseq))

if DNAseq == dna_rna.RNAtoDNA(RNAseq):
    print('The function worked')
else:
    print('The function did not work')