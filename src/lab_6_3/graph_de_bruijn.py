import utils

def graph_de_bruijn(strings):
    kmers = set()
    result = []
    for string in strings:
        kmers.add(string[1:])
        kmers.add(string[:-1])
    graph = {}
    for kmer in kmers:
        graph[kmer] = []
    for string in strings:
        graph[str(string[:-1])].append(str(string[1:]))

    for key, value in graph.items():
        if len(value) > 0:
            result.append(key + " -> " + ','.join(value))
    return result


if __name__ == '__main__':
    strings = utils.read_input_data()
    result = graph_de_bruijn(strings)
    utils.write_output_data(result)