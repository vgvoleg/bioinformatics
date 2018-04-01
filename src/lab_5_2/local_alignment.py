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


def local_alignment(v, w, score_matrix):
    n = len(v) + 1
    m = len(w) + 1
    s = [[0] * m for i in range(0, n)]

    for i in range(1, n):
        for j in range(1, m):
            vi = v[i - 1]
            wi = w[j - 1]
            s[i][j] = max( \
                0, \
                s[i - 1][j] - FORFEIT, \
                s[i][j - 1] - FORFEIT, \
                s[i - 1][j - 1] + utils.get_score(vi, wi, score_matrix) \
                )

    words = {"v": '', "w": ''}
    restore_words(words, s, v, w, n - 1, m - 1, False)
    words["v"] = words["v"][::-1]
    words["w"] = words["w"][::-1]
    score = calculate_score(words, score_matrix)
    return score, words


def restore_words(words, s, v, w, i, j, flag):
    if i == 0 and j == 0 or (s[i][j] == 0 and flag):
        return
    if i == 0:
        if flag:
            words["v"] += '-'
            words["w"] += w[j - 1]
        restore_words(words, s, v, w, i, j - 1, flag)
    elif j == 0:
        if flag:
            words["v"] += v[i - 1]
            words["w"] += '-'
        restore_words(words, s, v, w, i - 1, j, flag)
    elif s[i - 1][j - 1] > s[i - 1][j] - FORFEIT and s[i - 1][j - 1] > s[i][j - 1] - FORFEIT:
        words["v"] += v[i - 1]
        words["w"] += w[j - 1]
        restore_words(words, s, v, w, i - 1, j - 1, True)
    elif s[i - 1][j] >= s[i][j - 1]:
        if flag:
            words["v"] += v[i - 1]
            words["w"] += '-'
        restore_words(words, s, v, w, i - 1, j, flag)
    else:
        if flag:
            words["v"] += '-'
            words["w"] += w[j - 1]
        restore_words(words, s, v, w, i, j - 1, flag)


if __name__ == '__main__':
    v, w = utils.read_input_data()
    score_matrix = utils.read_scoring_matrix()
    score, words = local_alignment(v, w, score_matrix)
    utils.write_output_data(score, words)