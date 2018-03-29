import utils

FORFEIT = 5


def global_alignment(v, w, score_matrix):
    n = len(v) + 1
    m = len(w) + 1

    s = [[0] * m for i in range(0, n)]
    b = [['?'] * m for i in range(0, n)]

    for i in range(1, n):
        for j in range(1, m):
            vi = v[i - 1]
            wi = w[j - 1]

            s[i][j] = max( \
                s[i - 1][j] - FORFEIT, \
                s[i][j - 1] - FORFEIT, \
                s[i - 1][j - 1] + utils.get_score(vi, wi, score_matrix) \
            )
            if s[i][j] == s[i - 1][j - 1] + utils.get_score(vi, wi, score_matrix):
                b[i][j] = "↖"
            elif s[i][j] == s[i - 1][j] - FORFEIT:
                b[i][j] = "↑"
            else:
                b[i][j] = "←"

    words = {"v": '', "w": ''}
    restore_words(words, s, v, w, n - 1, m - 1)
    words["v"] = words["v"][::-1]
    words["w"] = words["w"][::-1]
    print(words)


def restore_words(words, s, v, w, i, j):
    if s[i - 1][j - 1] >= s[i - 1][j] and s[i - 1][j - 1] >= s[i][j - 1]:
        words["v"] += v[i - 1]
        words["w"] += w[j - 1]
        if i == 0:
            words["v"] += '-'
            return
        elif j == 0:
            words["w"] += '-'
            return
        restore_words(words, s, v, w, i - 1, j - 1)
    else:
        if i == 0 or j == 0:
            return
        if s[i - 1][j] >= s[i][j - 1]:
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
    global_alignment(v, w, score_matrix)