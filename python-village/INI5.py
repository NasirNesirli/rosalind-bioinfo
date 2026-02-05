"""
INI5: Working with Files
Problem: Print every other line from a file, starting with the first line.

Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file.
        (Assuming the first line is line 1.)
"""

# Open and read the input file
with open('data/INI5.txt', 'r') as file:
    for line in file:
        # Read all lines into a list, removing newline characters
        lines_list = file.read().splitlines()

text_length = len(lines_list)

# Print every other line (starting with index 0, which is line 1)
for i in range(text_length):
    if i % 2 == 0:
        print(lines_list[i])