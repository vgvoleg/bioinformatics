import utils

FORFEIT = 5

def calculate_score(words, score_matrix):
    l = len(words["v"])
    score = 0
    for i in range(0, l):
        if words["v"][i] == '-' or words["w"][i] == '-':
            score -= FORFEIT
        else:
            score += utils.get_score(words["v"][i], words["w"][i], score_matrix)
    return score

def global_alignment(v, w, score_matrix):
    n = len(v) + 1
    m = len(w) + 1
    s = [[0] * m for i in range(0, n)]

    for i in range(1, n):
        for j in range(1, m):
            vi = v[i - 1]
            wi = w[j - 1]
            s[i][j] = max( \
                s[i - 1][j] - FORFEIT, \
                s[i][j - 1] - FORFEIT, \
                s[i - 1][j - 1] + utils.get_score(vi, wi, score_matrix) \
            )

    words = {"v": '', "w": ''}
    restore_words(words, s, v, w, n - 1, m - 1)
    words["v"] = words["v"][::-1]
    words["w"] = words["w"][::-1]
    score = calculate_score(words, score_matrix)
    return score, words

def restore_words(words, s, v, w, i, j):
    if i == 0 and j == 0:
        return
    if i == 0:
        words["v"] += '-'
        words["w"] += w[j - 1]
        restore_words(words, s, v, w, i, j - 1)
    elif j == 0:
        words["v"] += v[i - 1]
        words["w"] += '-'
        restore_words(words, s, v, w, i - 1, j)
    elif s[i - 1][j - 1] >= s[i - 1][j] - FORFEIT and s[i - 1][j - 1] >= s[i][j - 1] - FORFEIT:
        words["v"] += v[i - 1]
        words["w"] += w[j - 1]
        restore_words(words, s, v, w, i - 1, j - 1)
    elif s[i - 1][j] >= s[i][j - 1]:
        words["v"] += v[i - 1]
        words["w"] += '-'
        restore_words(words, s, v, w, i - 1, j)
    else:
        words["v"] += '-'
        words["w"] += w[j - 1]
        restore_words(words, s, v, w, i, j - 1)


if __name__ == '__main__':
    v, w = utils.read_input_data()
    score_matrix = utils.read_scoring_matrix()
    score, words = global_alignment(v, w, score_matrix)
    utils.write_output_data(score, words)
