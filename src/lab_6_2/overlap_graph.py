import utils

class Word:
    def __init__(self, string):
        self.origin = string
        self.suffix = string[1:]
        self.prefix = string[:-1]

def overlap_graph(strings):
    words = [Word(string) for string in strings]
    result = []
    for i in range (0, len(words)):
        overlap_words = []
        for j in range (0, len(words)):
            if i != j and words[i].suffix == words[j].prefix:
                overlap_words.append(words[j].origin)
        if len(overlap_words) > 0:
            result.append(words[i].origin + " -> " + ','.join(overlap_words))
    return result

if __name__ == '__main__':
    strings = utils.read_input_data()
    result = overlap_graph(strings)
    utils.write_output_data(result)