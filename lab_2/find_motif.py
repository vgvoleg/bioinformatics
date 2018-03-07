from iterators import NMerIterator
import utils

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
        substrings = utils.get_substrings_by_pos(strings, t_size, pos)
        score = get_score(substrings, t_size)
        if score > best_score:
            best_score = score
            best_substrings = substrings

    return best_substrings


if __name__ == '__main__':
    t_size, n, strings = utils.read_input_data()
    result = find_motif(t_size, n, strings)
    utils.write_output_data(result)