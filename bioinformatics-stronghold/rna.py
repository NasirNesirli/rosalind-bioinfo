"""
RNA: Transcribing DNA into RNA
Problem: Convert a DNA string to RNA by replacing thymine with uracil.

In RNA, thymine (T) is replaced by uracil (U). All other bases remain the same.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

import sys
from pathlib import Path

# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file


def convert_dna_to_rna(dna_string: str):
    """
    Transcribe DNA to RNA by replacing thymine with uracil.
    
    Args:
        dna_string (str): A DNA sequence string
        
    Returns:
        str: The corresponding RNA sequence (T replaced with U)
    """
    rna_string: str = ' '
    # Replace each thymine (T) with uracil (U)
    for letter in dna_string:
        if letter == 'T':
            rna_string += 'U'
        else:
            rna_string += letter
    return rna_string


# Read DNA input, convert to RNA, and output
print(convert_dna_to_rna(read_txt_file('data/rosalind_rna.txt')))