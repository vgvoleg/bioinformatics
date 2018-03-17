def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        v = input_file.readline().strip()
        w = input_file.readline().strip()
    return v, w

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        output_file.write(result)