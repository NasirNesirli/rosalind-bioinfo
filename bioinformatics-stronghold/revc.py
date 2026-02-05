"""
REVC: Complementing a Strand of DNA
Problem: Find the reverse complement of a DNA string.

In DNA, adenine (A) pairs with thymine (T), and cytosine (C) pairs with guanine (G).
The reverse complement is formed by complementing each base and then reversing the string.

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement of s.
"""

import sys
from pathlib import Path

# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file


def reverse_complement(dna_string: str):
    """
    Generate the reverse complement of a DNA string.
    
    Complements each nucleotide (A↔T, G↔C) and reverses the string.
    
    Args:
        dna_string (str): A DNA sequence string
        
    Returns:
        str: The reverse complement of the input DNA string
    """
    complement_dna: str = ''
    # Build complement by replacing each base with its pair
    for letter in dna_string:
        if letter == 'A':
            complement_dna += 'T'
        if letter == 'T':
            complement_dna += 'A'
        if letter == 'G':
            complement_dna += 'C'
        if letter == 'C':
            complement_dna += 'G'
    # Reverse the complemented string
    return complement_dna[::-1]


# Read input, compute reverse complement, and output
print(reverse_complement(read_txt_file('data/rosalind_revc.txt')))