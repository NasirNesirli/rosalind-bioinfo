"""
Utility functions for Rosalind bioinformatics problems.
"""


def read_txt_file(filename):
    """
    Read the entire contents of a text file.
    
    Args:
        filename (str): Path to the text file to read
        
    Returns:
        str: The complete contents of the file as a string
    """
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content