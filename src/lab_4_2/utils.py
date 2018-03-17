def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        n, m = list(int(s) for s in lines[0].split(' '))
        s_cost = []
        w_cost = []
        for i in range(1, m+1):
            values = list(int(s) for s in lines[i].split(' '))
            s_cost.append(values)
        for i in range(m+2, n + m + 3):
            values = list(int(s) for s in lines[i].split(' '))
            w_cost.append(values)

    return n + 1, m + 1, s_cost, w_cost

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(result))