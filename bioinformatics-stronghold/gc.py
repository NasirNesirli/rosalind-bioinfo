# Identifying Unknown DNA Quickly

# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. 
# A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# Sample Dataset
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# Sample Output
# Rosalind_0808
# 60.919540

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file

dna_string = read_txt_file('data/rosalind_gc.txt')

def parse_fasta(dna_string):
    sequences = {}
    for record in dna_string.strip().split('>'):
        if record is not None and record != '':
            sequences[record[:13]] = record[13:].replace('\n', '')
    return sequences
    

sequences = parse_fasta(dna_string)

def gc_content(sequences):
    gc_contents = {}
    for sequence_name, sequence_content in sequences.items():
        gc_count = sequence_content.count('G') + sequence_content.count('C')
        gc_percentage = (gc_count / len(sequence_content)) * 100
        gc_contents[sequence_name] = gc_percentage
    return gc_contents

gc_contents = gc_content(sequences)
max_gc_index_name = max(gc_contents, key=gc_contents.get)
print(max_gc_index_name)
print(f"{gc_contents[max_gc_index_name]:.6f}")