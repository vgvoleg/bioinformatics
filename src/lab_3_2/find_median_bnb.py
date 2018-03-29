from iterators import DNAWordTree
import utils


def get_score(strings, word):
    word_size = len(word)
    score = 0
    for string in strings:
        min_score = float('inf')
        for i in range(0, len(string) - word_size + 1):
            ne = 0
            for j in range(0, word_size):
                if string[i+j] != word[j]:
                    ne += 1
            if ne < min_score:
                min_score = ne
        score += min_score
    return score


def bounds_and_branches_median_search(t, strings):
    best_score = float('inf')
    best_word = []
    searchTree = DNAWordTree(t)
    i = 0
    while i > -1:
        if i < t - 1:
            word = searchTree.current_word(i)
            optimistic_score = get_score(strings, word)
            if optimistic_score > best_score:
                i = searchTree.bypass_move(i)
            else:
                i = searchTree.next_vertex(i)
        else:
            word = searchTree.current_word(t)
            score = get_score(strings, word)
            if score < best_score:
                best_score = score
                best_word = word
            i = searchTree.next_vertex(i)
    return ''.join(best_word)


if __name__ == '__main__':
    t, strings = utils.read_input_data()
    result = bounds_and_branches_median_search(t, strings)
    utils.write_output_data(result)