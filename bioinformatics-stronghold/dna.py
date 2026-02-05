import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file


def count_nucleotides(dna_string):
    letter_counts = {}
    for letter in dna_string:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts


letter_counts = count_nucleotides(read_txt_file('data/rosalind_dna.txt'))

print(letter_counts['A'], letter_counts['C'], letter_counts['G'], letter_counts['T'])