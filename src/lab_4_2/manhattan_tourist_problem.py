import utils


def manhattan_tourist(n, m, s_cost, w_cost):
    s = list([0]*m for i in range(0,n))
    for i in range(1, n):
        s[i][0] = s[i-1][0] + s_cost[i-1][0]
    for j in range(1, m):
        s[0][j] = s[0][j-1] + w_cost[0][j-1]

    for i in range(1, n):
        for j in range(1, m):
            s[i][j] = max(s[i-1][j] + s_cost[i-1][j],\
                          s[i][j-1] + w_cost[i][j-1])

    return s[n-1][m-1]

if __name__ == '__main__':
    n, m, s_cost, w_cost = utils.read_input_data()
    result = manhattan_tourist(n, m, s_cost, w_cost)
    utils.write_output_data(result)