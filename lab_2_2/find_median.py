from iterators import DNAIterator
import utils

def get_score(strings, word, t_size):
    score = 0
    for string in strings:
        min_score = float('inf')
        for i in range(0, len(string) - t_size):
            ne = 0
            for j in range(0, t_size):
                if string[i+j] != word[j]:
                    ne += 1
            if ne < min_score:
                min_score = ne
        score += min_score
    return score


def find_median(t_size, strings):
    best_score = float('inf')
    best_word = None
    iterator = DNAIterator(t_size)
    while iterator.has_next():
        word = iterator.next()
        score = get_score(strings, word, t_size)
        if score < best_score:
            best_score = score
            best_word = word[:]
    return ''.join(best_word)


if __name__ == '__main__':
    t_size, strings = utils.read_input_data()
    result = find_median(t_size, strings)
    utils.write_output_data(result)