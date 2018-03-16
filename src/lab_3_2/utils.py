def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        t_size = int(lines[0])
        strings = []
        for i in range (1, len(lines)):
            strings.append(lines[i].rstrip())
    return t_size, strings

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        output_file.write(result)