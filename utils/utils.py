def read_txt_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content