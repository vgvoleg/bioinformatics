import utils

def string_spectre(k, string):
    return [''.join(string[i:i+k]) for i in range(0, len(string) - k + 1)]

if __name__ == '__main__':
    k, string = utils.read_input_data()
    result = string_spectre(k, string)
    utils.write_output_data(result)