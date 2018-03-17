import utils


def lcs(v, w):
    n = len(v) + 1
    m = len(w) + 1

    s = [[0] * m for i in range(0, n)]
    b = [['?'] * m for i in range(0, n)]

    for i in range(1, n):
        for j in range(1, m):
            s[i][j] = max( \
                s[i - 1][j], \
                s[i][j - 1], \
                s[i - 1][j - 1] + 1 if v[i - 1] == w[j - 1] else -1 \
            )
            if v[i - 1] == w[j - 1]:
                b[i][j] = "↖"
            elif s[i][j] == s[i - 1][j]:
                b[i][j] = "↑"
            else:
                b[i][j] = "←"

    substring = []
    build_substring(substring, b, v, n - 1, m - 1)

    return ''.join(substring)


def build_substring(sub, b, v, i, j):
    if i == j == 0:
        return
    if b[i][j] == "↖":
        sub.insert(0, v[i - 1])
        build_substring(sub, b, v, i - 1, j - 1)
    else:
        if b[i][j] == "↑":
            build_substring(sub, b, v, i - 1, j)
        else:
            build_substring(sub, b, v, i, j - 1)


if __name__ == '__main__':
    v, w = utils.read_input_data()
    result = lcs(v, w)
    utils.write_output_data(result)
