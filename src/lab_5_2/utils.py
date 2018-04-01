def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        v = input_file.readline().strip()
        w = input_file.readline().strip()
    return v, w


def read_scoring_matrix():
    result = []
    with open('PAM250.txt', encoding='utf-8') as input_file:
        input_file.readline()
        for i in range(0, 20):
            result_line = []
            line = input_file.readline().strip()
            values = line.split(" ")[1:]
            for value in values:
                if value != '':
                    result_line.append(int(value))
            result.append(result_line)
    return result

letters = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']


def get_score(vi, wi, matrix):
    i = letters.index(vi)
    j = letters.index(wi)
    return matrix[i][j]


def write_output_data(score, words):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(score) + "\n")
        output_file.write(words["v"] + "\n")
        output_file.write(words["w"])


if __name__ == '__main__':
    matrix = read_scoring_matrix()
    print(get_score('A', 'Q', matrix))