"""
GC: Computing GC Content
Problem: Identifying Unknown DNA Quickly

The GC-content of a DNA string is given by the percentage of symbols in the string 
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.

DNA strings must be labeled when they are consolidated into a database. A commonly 
used method of string labeling is called FASTA format. In this format, the string 
is introduced by a line that begins with '>', followed by some labeling information.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the 
        GC-content of that string.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
"""

import sys
from pathlib import Path

# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.utils import read_txt_file

# Read the FASTA format input file
dna_string = read_txt_file('data/rosalind_gc.txt')


def parse_fasta(dna_string):
    """
    Parse a FASTA format string into a dictionary of sequences.
    
    Args:
        dna_string (str): Multi-line string in FASTA format
        
    Returns:
        dict: Dictionary mapping sequence IDs to their DNA sequences
    """
    sequences = {}
    # Split by '>' to separate individual FASTA records
    for record in dna_string.strip().split('>'):
        if record is not None and record != '':
            # Extract sequence ID (first 13 characters) and sequence content
            # Remove newlines from the sequence
            sequences[record[:13]] = record[13:].replace('\n', '')
    return sequences


# Parse the input FASTA data
sequences = parse_fasta(dna_string)


def gc_content(sequences):
    """
    Calculate GC content percentage for each DNA sequence.
    
    GC content is the percentage of nucleotides that are either G or C.
    
    Args:
        sequences (dict): Dictionary mapping sequence IDs to DNA sequences
        
    Returns:
        dict: Dictionary mapping sequence IDs to their GC content percentages
    """
    gc_contents = {}
    for sequence_name, sequence_content in sequences.items():
        # Count G and C nucleotides
        gc_count = sequence_content.count('G') + sequence_content.count('C')
        # Calculate percentage
        gc_percentage = (gc_count / len(sequence_content)) * 100
        gc_contents[sequence_name] = gc_percentage
    return gc_contents


# Calculate GC content for all sequences
gc_contents = gc_content(sequences)

# Find the sequence with the highest GC content
max_gc_index_name = max(gc_contents, key=gc_contents.get)

# Output the result
print(max_gc_index_name)
print(f"{gc_contents[max_gc_index_name]:.6f}")