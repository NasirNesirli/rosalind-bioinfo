with open('data/INI5.txt', 'r') as file:
    for line in file:
        lines_list = file.read().splitlines()

text_length = len(lines_list)

for i in range(text_length):
    if i % 2 == 0:
        print(lines_list[i])