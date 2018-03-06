from iterators import NMerIterator

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

def get_score(substrings, t_size):
    score = 0
    n = len(substrings)
    for i in range(0, t_size):
        dna = {'C':0, 'A':0, 'G':0, 'T':0}
        for j in range(0, n):
            dna[substrings[j][i]] += 1
        score += dna[max(dna, key=dna.get)]
    return score

def find_motif(t_size, n, strings):
    best_score = 0
    best_substrings = None
    string_size = len(strings[0])
    iterator = NMerIterator(n, string_size - t_size)
    while iterator.has_next():
        pos = iterator.next()
        substrings = get_substrings_by_pos(strings, t_size, pos)
        score = get_score(substrings, t_size)
        if score > best_score:
            best_score = score
            best_substrings = substrings

    return best_substrings


if __name__ == '__main__':
    t_size, n, strings = read_input_data()
    result = find_motif(t_size, n, strings)
    write_output_data(result)