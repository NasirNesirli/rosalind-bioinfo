import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file


def convert_dna_to_rna(dna_string: str):
    rna_string: str = ' '
    for letter in dna_string:
        if letter == 'T':
            rna_string += 'U'
        else:
            rna_string += letter
    return rna_string

print(convert_dna_to_rna(read_txt_file('data/rosalind_rna.txt')))