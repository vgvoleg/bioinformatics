def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        return [line.strip() for line in input_file.readlines()]

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        for line in result:
            output_file.write(line + "\n")