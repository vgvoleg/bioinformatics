def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        money = int(input_file.readline())
        coins_list = input_file.readline()
        coins = list(int(s) for s in coins_list.split(','))
    return money, coins

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(result))