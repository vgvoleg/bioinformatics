import utils

FORFEIT = 5

def local_alignment(v, w, score_matrix):
    n = len(v) + 1
    m = len(w) + 1
    s = [[0] * m for i in range(0, n)]
    b = [["↯"] * m for i in range(0, n)]

    max_elem = {"score": 0, "i": 0, "j": 0}

    for i in range(1, n):
        for j in range(1, m):
            if i == n - 1 and j == m - 1:
                s[i][j] = max_elem["score"]
            vi = v[i - 1]
            wi = w[j - 1]
            s[i][j] = max( \
                0, \
                s[i - 1][j] - FORFEIT, \
                s[i][j - 1] - FORFEIT, \
                s[i - 1][j - 1] + utils.get_score(vi, wi, score_matrix) \
                )

            if s[i][j] >= max_elem["score"]:
                max_elem["score"] = s[i][j]
                max_elem["i"] = i
                max_elem["j"] = j

            if s[i][j] == s[i - 1][j - 1] + utils.get_score(vi, wi, score_matrix):
                b[i][j] = "↖"
            elif s[i][j] == s[i - 1][j] - FORFEIT:
                b[i][j] = "↑"
            elif s[i][j] == s[i][j - 1] - FORFEIT:
                b[i][j] = "←"
            else:
                b[i][j] = "↯"

    words = {"v": '', "w": ''}
    restore_words(words, b, v, w, max_elem["i"], max_elem["j"])
    words["v"] = words["v"][::-1]
    words["w"] = words["w"][::-1]
    return max_elem["score"], words


def restore_words(words, b, v, w, i, j):
    if b[i][j] == "↯":
        return
    elif b[i][j] == "↖":
        words["v"] += v[i - 1]
        words["w"] += w[j - 1]
        restore_words(words, b, v, w, i - 1, j - 1)
    elif b[i][j] == "←":
        words["v"] += '-'
        words["w"] += w[j - 1]
        restore_words(words, b, v, w, i, j - 1)
    else:
        words["v"] += v[i - 1]
        words["w"] += '-'
        restore_words(words, b, v, w, i - 1, j)


if __name__ == '__main__':
    v, w = utils.read_input_data()
    score_matrix = utils.read_scoring_matrix()
    score, words = local_alignment(v, w, score_matrix)
    utils.write_output_data(score, words)