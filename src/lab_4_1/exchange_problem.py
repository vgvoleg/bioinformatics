import utils


def dp_change(money, coins):
    best_num_coins = [0]*money
    for m in range(0, money):
        if m + 1 in coins:
            best_num_coins[m] = 1
            continue
        best_num_coins[m] = float('inf')
        for coin in coins:
            if m + 1 >= coin:
                a = best_num_coins[m-coin] + 1
                best_num_coins[m] = min(best_num_coins[m], a)

    return best_num_coins[money - 1]

if __name__ == '__main__':
    money, coins = utils.read_input_data()
    result = dp_change(money, coins)
    utils.write_output_data(result)