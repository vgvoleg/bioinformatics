from iterators import StartIndexesTree
import utils

def get_score(substrings, n, t_size):
    score = 0
    for i in range(0, t_size):
        dna = {'C':0, 'A':0, 'G':0, 'T':0}
        for j in range(0, n):
            dna[substrings[j][i]] += 1
        score += dna[max(dna, key=dna.get)]
    return score

def bounds_and_branches_motif_search(t, n, DNA):
    string_size = len(DNA[0])
    searchTree = StartIndexesTree(n, string_size - t)
    best_score = 0
    best_subs = []
    i = 0
    while i > -1:
        substrings = utils.get_substrings_by_pos(DNA, t, searchTree.current_indexes())
        if i < n - 1:
            optimistic_score = get_score(substrings, i, t) + (n-i)*t
            if optimistic_score < best_score:
                i = searchTree.bypass_move(i)
            else:
                i = searchTree.next_vertex(i)
        else:
            score = get_score(substrings, n, t)
            if score > best_score:
                best_score = score
                best_subs = substrings[:]
            i = searchTree.next_vertex(i)
    return best_subs

if __name__ == "__main__":
    t, n, DNA = utils.read_input_data()
    result = bounds_and_branches_motif_search(t, n, DNA)
    utils.write_output_data(result)
