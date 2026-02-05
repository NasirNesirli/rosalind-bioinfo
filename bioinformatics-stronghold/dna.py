"""
DNA: Counting DNA Nucleotides
Problem: Count the number of each nucleotide (A, C, G, T) in a DNA string.

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times 
        that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

import sys
from pathlib import Path

# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file


def count_nucleotides(dna_string):
    """
    Count the occurrences of each nucleotide in a DNA string.
    
    Args:
        dna_string (str): A DNA sequence containing A, C, G, T nucleotides
        
    Returns:
        dict: Dictionary with nucleotide counts {nucleotide: count}
    """
    letter_counts = {}
    for letter in dna_string:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts


# Read input and count nucleotides
letter_counts = count_nucleotides(read_txt_file('data/rosalind_dna.txt'))

# Output the counts in required order: A C G T
print(letter_counts['A'], letter_counts['C'], letter_counts['G'], letter_counts['T'])