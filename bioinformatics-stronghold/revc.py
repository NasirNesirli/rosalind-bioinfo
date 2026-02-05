import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file

def reverse_complement(dna_string: str):
    complement_dna: str = ''
    for letter in dna_string:
        if letter == 'A':
            complement_dna += 'T'
        if letter == 'T':
            complement_dna += 'A'
        if letter == 'G':
            complement_dna += 'C'
        if letter == 'C':
            complement_dna += 'G'
    return complement_dna[::-1]


print(reverse_complement(read_txt_file('data/rosalind_revc.txt')))