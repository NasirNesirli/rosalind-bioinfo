with open('data/INI6.txt', 'r') as file:
    file_content = file.read()

file_content_list = file_content.split(' ')

word_counts = {}

for word in file_content_list:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

for key, value in word_counts.items():
    print(key, value)