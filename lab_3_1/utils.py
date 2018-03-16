def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        t_size, n = list(map(int, input_file.readline().split(" ")))
        strings = []
        for i in range(0, n):
            strings.append(input_file.readline().rstrip())
    return t_size, n, strings

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        for i in range(0, len(result)):
            output_file.write(result[i]+'\n')

def get_substrings_by_pos(strings, t_size, pos):
    substrings = []
    for i in range(0, len(strings)):
        j = pos[i]
        substrings.append(strings[i][j:j+t_size])
    return substrings
