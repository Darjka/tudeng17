#!/usr/bin/env python3
"""
loeb fasta faili ja leiab komplementaarse ahela
"""
__author__ = "Mina Ise"
__copyright__ = "Copyright 2015, Minufirma"
__credits__ = ["Mina Ise", "Minu Sober", "Tema Sober"]
__version__ = "0.2"
__email__ = "Mina.Ise@gmail.com"





from __future__ import division
from __future__ import print_function
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO


def read_fasta(): #see funktsioon avab fasta faili ja annab Seq formaadis sekventsi
    sequence = SeqIO.read("example.fasta", "fasta", IUPAC.unambiguous_dna)
    return(sequence)




def main():
# k6ige pealt avatakse fasta fail, funktsiooniga "read_fasta" ja leitakse komplementaarne ahel funktsiooniga "reverse_complement"
    template = read_fasta().reverse_complement()
    print(template.seq)
    return(template.seq)

	
	
if __name__ == "__main__":
    main()

