"""
INI6: Dictionaries
Problem: Count the occurrences of each word in a text file.

Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are 
        separated by spaces. Each output line should contain a word and its count.
"""

# Open and read the entire file content
with open('data/INI6.txt', 'r') as file:
    file_content = file.read()

# Split content into words (space-separated)
file_content_list = file_content.split(' ')

# Dictionary to store word counts
word_counts = {}

# Count occurrences of each word
for word in file_content_list:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Print each word and its count
for key, value in word_counts.items():
    print(key, value)